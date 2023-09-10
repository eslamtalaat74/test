odoo.define("sh_electronic_pos_qr_saudi.pos", function (require) {
    "use strict";

    var models = require("point_of_sale.models");
    var DB = require("point_of_sale.DB");
    const Registries = require("point_of_sale.Registries");
    const ReceiptScreen = require("point_of_sale.ReceiptScreen");
    const { useRef, useContext } = owl.hooks;
    var core = require('web.core');
    var _t = core._t;
    const OrderReceipt = require('point_of_sale.OrderReceipt')
    const PosComponent = require("point_of_sale.PosComponent")
    const ProductScreen = require("point_of_sale.ProductScreen");
    const { useListener } = require("web.custom_hooks");
    const AbstractAwaitablePopup = require("point_of_sale.AbstractAwaitablePopup");

    models.load_models({
        model: "sh.pos.config.qr.elements",
        label: "load_qr_elements",
        loaded: function (self, All_qr_elemet) {
            self.db.all_qr_elemets = All_qr_elemet;
            if (All_qr_elemet && All_qr_elemet.length > 0) {
                _.each(All_qr_elemet, function (each_qr_element) {
                    self.db.qr_elemet_by_id[each_qr_element.id] = each_qr_element
                });
            }
        },
    })
    models.load_fields('res.company', ['sh_arabic_name', 'street', 'city', 'zip', 'arabic_street', 'arabic_street2', 'arabic_city', 'arabic_zip'])
    models.load_fields('res.partner', ['sh_cr_no'])
    models.load_fields('product.product', ['sh_arabic_name'])
    models.load_fields('pos.payment.method', ['sh_payment_method_arabic_name'])

    DB.include({
        init: function (options) {
            this._super.apply(this, arguments);
            this.qr_elemet_by_id = {};
        },
    });

    var _super_Orderline = models.Orderline.prototype;
    models.Orderline = models.Orderline.extend({
        export_for_printing: function () {
            var res = _super_Orderline.export_for_printing.apply(this, arguments)
            res['sh_arabic_name'] = this.get_product().sh_arabic_name;
            res['line_note'] = this.note;
            return res
        }
    })

    var _super_Paymentline = models.Paymentline.prototype;
    models.Paymentline = models.Paymentline.extend({
        export_for_printing: function () {
            var res = _super_Paymentline.export_for_printing.apply(this, arguments)
            res['sh_payment_method_arabic_name'] = this.payment_method.sh_payment_method_arabic_name
            return res
        }
    });

    const PosResOrderReceipt = (ReceiptScreen) =>
    class extends ReceiptScreen {
        constructor() {
            super(...arguments)
            this.shorderReceipt = useRef('order-receipt');
        }
        compute_sa_qr_code(name, vat, date_isostring, amount_total, amount_tax) {
            /* Generate the qr code for Saudi e-invoicing. Specs are available at the following link at page 23
            https://zatca.gov.sa/ar/E-Invoicing/SystemsDevelopers/Documents/20210528_ZATCA_Electronic_Invoice_Security_Features_Implementation_Standards_vShared.pdf
            */
            const seller_name_enc = this._compute_qr_code_field(1, name);
            const company_vat_enc = this._compute_qr_code_field(2, vat);
            const timestamp_enc = this._compute_qr_code_field(3, date_isostring);
            const invoice_total_enc = this._compute_qr_code_field(4, amount_total.toString());
            const total_vat_enc = this._compute_qr_code_field(5, amount_tax.toString());

            const str_to_encode = seller_name_enc.concat(company_vat_enc, timestamp_enc, invoice_total_enc, total_vat_enc);

            let binary = '';
            for (let i = 0; i < str_to_encode.length; i++) {
                binary += String.fromCharCode(str_to_encode[i]);
            }
            return btoa(binary);
        }

        _compute_qr_code_field(tag, field) {
            const textEncoder = new TextEncoder();
            const name_byte_array = Array.from(textEncoder.encode(field));
            const name_tag_encoding = [tag];
            const name_length_encoding = [name_byte_array.length];
            return name_tag_encoding.concat(name_length_encoding, name_byte_array);
        }
        mounted() {
            var self = this;
            var dic = {}
            var is_gcc_country = ['SA', 'AE', 'BH', 'OM', 'QA', 'KW'].includes(self.env.pos.company.country.code);
            if (self.env.pos.config.display_qr_code && is_gcc_country) {
                $('.pos-receipt-container').addClass('sh_receipt_content')
            }
            if (_t.database.parameters.direction) {
                $('.sh_receipt_content').css('direction', 'ltr')
            }
            var qr_code = this.compute_sa_qr_code(self.env.pos.company.name, self.env.pos.company.vat, self.env.pos.get_order().export_for_printing().date.isostring, self.env.pos.get_order().export_for_printing().total_with_tax, self.env.pos.get_order().export_for_printing().total_tax);
            
            if ($('#qr_image') && $('#qr_image').length > 0) {
                // Create QRCode Object

                var div = document.createElement('div')
                new QRCode(div, { text: qr_code });

                var can = $(div).find('canvas')[0]
                var img = new Image();
                img.src = can.toDataURL();

                $(img).css({ 'height': self.env.pos.config.qr_code_height, 'width': self.env.pos.config.qr_code_width })

                $('#qr_image').append(img)

            }
            
            super.mounted()
        }
        async _sendReceiptToCustomer() {
            super._sendReceiptToCustomer(this, arguments)
            const receiptString = this.shorderReceipt.comp.el.outerHTML;
        }
    };
    Registries.Component.extend(ReceiptScreen, PosResOrderReceipt);
    
    class ReturnBtn extends PosComponent {
        constructor() {
            super(...arguments)
            useListener('click-return-button', this.onClickButton)
        }
        onClickButton() {
        	var self = this;
            var order = self.env.pos.get_order()
            if(order && order.get_orderlines() && order.get_orderlines().length > 0){            	
            	self.showPopup("return_order_popup");
            }else{
            	alert("Please enter product in cart.")
            }
        }
    }
    ReturnBtn.template = 'ReturnBtn';
    ProductScreen.addControlButton({
        component: ReturnBtn,
        condition: function () {
            return this.env.pos.config.display_qr_code && this.env.pos.config.sh_allow_return;
        }
    })
    Registries.Component.add(ReturnBtn)
    
    class return_order_popup extends AbstractAwaitablePopup {
        constructor() {
            super(...arguments);
        }
        confirm(){
        	var self = this;
        	if($('.return_order_textbox') && $('.return_order_textbox').val()){
            	self.env.pos.get_order().set_refunded_order_ref($('.return_order_textbox').val())
        		this.trigger("close-popup");
            }else{
            	alert("Enter Return Order Reference")
            }
        }
    }
    return_order_popup.template = "return_order_popup";

    Registries.Component.add(return_order_popup);
    
    var _super_order = models.Order.prototype;
    models.Order = models.Order.extend({
    	initialize: function (attributes, options) {
            this.return_order_ref = false;
            _super_order.initialize.apply(this, arguments);
        },
        set_refunded_order_ref: function (return_order_ref) {
        	this.return_order_ref = return_order_ref;
        },
        get_refunded_order_ref: function () {
            return this.return_order_ref;
        },
        export_as_JSON: function () {
            var new_val = {};
            var orders = _super_order.export_as_JSON.call(this);
            new_val = {
            		refunded_order_ref: this.get_refunded_order_ref(),
            };
            $.extend(orders, new_val);
            return orders;
        },
    });
    
});
