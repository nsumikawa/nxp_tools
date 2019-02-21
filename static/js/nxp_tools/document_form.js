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
var document_html_class

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
    this.form.elements.name.value = ''

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

            if( self.document_id == 'None' ){
              document_html_class.add( data.id, data.type, data.author, data.name )
            } else {
              document_html_class.replace( data.id, data.type, data.author, data.name )
            }

            category_form_class.populate_element_div( [[data.id, data.name, data.description]] )

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

    $('#document_' + this.document_id ).remove()

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







class document_html {

  constructor( element_id ){
    // this.parent = parent; //$("#product_id")
    this.element_id = element_id;
  }

  show(){ document.getElementById(this.element_id + '_container').style.display='Block'}
  hide(){ document.getElementById(this.element_id + '_container').style.display='None'}
  clear(){ document.getElementById(this.element_id).innerHTML = ""}


  add_multiple( data ){
    // add elements to the element block in the category form

    for (var i = 0; i < data.length; i++) {
      var id = data[i][0];
      var type = data[i][1];
      var author = data[i][2];
      var name = data[i][5];

      this.add(id, type, author, name )

    }
  }


  add( id, type, author, name ){
    //adds the document to the html
    console.log( this.element_id )
    console.log( document_html_class.element_id )
    document.getElementById(this.element_id).innerHTML += this._markup(id, type, author, name )
  }

  replace( id, type, author, name ){
    //removes the current document and replaces it with a new one
    $(`#document_${id}` ).remove()
    this.add( id, type, author, name )
  }

  _color( type ){
    //returns the badge color based on the specified type
    if( type == 'Video' ){ return 'badge-primary' }
    if( type == 'Powerpoint' ){ return 'badge-warning' }
    if( type == 'PDF' ){ return 'badge-danger' }
    if( type == 'Link' ){ return 'badge-info' }
    if( type == 'Template' ){ return 'badge-success' }
    return 'badge-default'

  }

  _text( type ){
    //returns the text based on the specified type
    if( type == 'Video' ){ return 'Video' }
    if( type == 'Powerpoint' ){ return 'PPTx' }
    if( type == 'PDF' ){ return 'PDF' }
    if( type == 'Link' ){ return 'Link' }
    if( type == 'Template' ){ return 'Temp' }
    return ''
  }


  _padding( type ){
    //returns the text based on the specified type
    if( type == 'Video' ){ return '10px' }
    if( type == 'Powerpoint' ){ return '15px' }
    if( type == 'PDF' ){ return '19px' }
    if( type == 'Link' ){ return '10px' }
    if( type == 'Template' ){ return '10px' }
    return ''
  }


  _markup(id, type, author, name ){
    // returns the markup for the document badge

    var color = this._color( type )
    var text = this._text( type )
    var padding = this._padding( type )

    return `
            <div class="col" align='left' id='document_${id}'>
              <span class="badge badge-pill ${color}"
                    onclick="document_form_class.pull(${id})"
                    style="padding-right:10px">
                    ${text}
                    <i class="fa fa-edit" style="padding-left:${padding}"></i>
              </span>
              <span style='padding-left:10px;'> <b>${name}</b> by ${author}</span>
            </div>
            `



  }

}
