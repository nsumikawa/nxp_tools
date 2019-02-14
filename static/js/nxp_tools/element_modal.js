/*
Element_modal.js
=======

description
-----------
Routines for manipulating and rendering the element modal

Author : Nik Sumikawa
Date : Feb 13, 2019

*/


var element_modal_html_class

class element_modal_html {

  constructor( modal, table ){
    this.modal = modal;
    this.table = table;
  }

  open( element_id ){
    // populates the entire page with categories

    var self = this

    //ajax request to push content to the database.
    $.ajax({
        url: url_prefix() + '/ajax/views/element/pull',
        data: { 'id' : element_id,
                },
        success: function (data) {

          $('#element_name').html( data.name )
          $('#element_description').html( data.description )

          //add documents to the table
          element_modal_html_class.table.find('tbody').empty();
          for (var i = 0; i < data.document.length; i++) {
            self.add( data.document[i]);
          }

          document.getElementById(element_modal_html_class.modal).style.display='Block'

        },
        error: function(data) {
            $("#MESSAGE-DIV").html("Something went wrong!");
        }
    });
    return false;

  };

  add( document ){
    //adds a single item to the document

    var _markup = this.markup( document[0], document[1], document[2], document[3], document[4] )
    element_modal_html_class.table.find('tbody').append( _markup );

  }



  markup( id, type, user, link, date ){

    var image_markup = ''
    if( type == 'Video' ){ image_markup = '<i class="fas fa-video"></i> Watch' }
    if( type == 'Powerpoint' ){ image_markup = '<i class="fas fa-file-powerpoint"></i> Open' }
    if( type == 'PDF' ){ image_markup = '<i class="fas fa-file-pdf"></i> Open' }


    var button_markup = ` <a class="btn btn-primary btn-round" role="button" href="${link}">
                          ${image_markup}
                        </a>
                        `
    if ( date != null ){ var datestring = date.toString().split('T')[0]; }

    return   `
            <tr id=${id}>
              <th id='type'>${button_markup}</th>
              <th id='user'>${user} </th>
              <th id='user'>${datestring}</th>
            </tr>
            `

  }



}
