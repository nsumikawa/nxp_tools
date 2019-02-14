/*
Document.js
=======

description
-----------
Routines for manipulating and rendering the document form

Author : Nik Sumikawa
Date : Feb 13, 2019

*/


var document_form_class

class document_form {

  constructor( modal, form, form_name ){
    this.modal = modal;
    this.form = form;
    this.form_name = form_name;
    this.document_id = 'None';
  }

  new( element = ''){
    //clears the contents of the html form

    //clear the element id
    this.document_id = 'None'

    //clear the form content
    this.form.elements.element.value = element
    this.form.elements.type.value = ''
    this.form.elements.link.value = ''

    document.getElementById(this.modal).style.display='Block'
  }

  push( ){
    // populates and shows the  modal with all events corresponding to the product

    var self = this

    // add the document id to the form
    $('<input>').attr({
        type: 'hidden',
        name: 'id',
        value: this.document_id
    }).appendTo( '#' + this.form_name );

    //ajax request to push content to the database.
    $.ajax({
        type: $( '#' + this.form_name ).attr('method'),
        url: url_prefix() + '/ajax/views/document/push',
        data: $( '#' + this.form_name ).serialize(),
        success: function (data) {
            //update the current page on return

            // if( self.document_id == 'None' ){
            //   element_html_class.add( data.category_id, data.id, data.name, data.description )
            // } else {
            //   element_html_class.replace( data.id, data.name, data.description )
            // }
            //
            // category_form_class.populate_element_div( [[data.id, data.name, data.description]] )

            document.getElementById(document_form_class.modal).style.display='None'
        },
        error: function(data) {
            $("#MESSAGE-DIV").html("Something went wrong!");
        }
    });
    return false;

  };

  pull( document_id ){
    // populates and shows the  modal with all events corresponding to the product

    // set the global value for the document id
    this.document_id = document_id


    //ajax request to push content to the database.
    $.ajax({
        url: url_prefix() + '/ajax/views/document/pull',
        data: {'id':document_id},
        success: function (data) {
            //update the form content
            document_form_class.form.elements.element.value = data.element
            document_form_class.form.elements.type.value = data.type
            document_form_class.form.elements.link.value = data.link

            document.getElementById(document_form_class.modal).style.display='Block'
        },
        error: function(data) {
            $("#MESSAGE-DIV").html("Something went wrong!");
        }
    });
    return false;

  };

  delete( ){
    // populates and shows the  modal with all events corresponding to the product

    $('#category_' + this.document_id ).remove()

    document.getElementById(document_form_class.modal).style.display='None'

    //ajax request to push content to the database.
    $.ajax({
        url: url_prefix() + '/ajax/views/document/delete',
        data: {'id':this.document_id},
        success: function (data) {
          //TODO remove contents from the page
          document.getElementById(document_form_class.modal).style.display='None'
        },
        error: function(data) {
            $("#MESSAGE-DIV").html("Something went wrong!");
        }
    });
    return false;

  };


}
