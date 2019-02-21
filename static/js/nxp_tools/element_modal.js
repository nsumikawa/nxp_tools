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

  constructor( modal, doc_table, doc_div, temp_table, temp_div ){
    this.modal = modal;
    this.doc_table = doc_table;
    this.doc_div = doc_div;
    this.temp_table = temp_table;
    this.temp_div = temp_div;
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


          //populate the template table when it exists
          if( data.document.length > 0 ){
            //add documents to the table
            self.doc_table.find('tbody').empty();
            for (var i = 0; i < data.document.length; i++) {
              self.add( data.document[i], self.doc_table );
            }

            document.getElementById(self.doc_div).style.display='Block'

          //hide the table when no data exists
          }else{ document.getElementById(self.doc_div).style.display='None' }



          //populate the template table when it exists
          if( data.template.length > 0 ){
            //clear and then populate the table when data exists
            self.temp_table.find('tbody').empty();
            for (var i = 0; i < data.template.length; i++) {
              self.add( data.template[i], self.temp_table );
            }

            document.getElementById(self.temp_div).style.display='Block'

          //hide the table when no data exists
          }else{ document.getElementById(self.temp_div).style.display='None' }


          //unhide/show the modal
          document.getElementById(element_modal_html_class.modal).style.display='Block'

        },
        error: function(data) {
            $("#MESSAGE-DIV").html("Something went wrong!");
        }
    });
    return false;

  };

  add( document, table ){
    //adds a single item to the document

    var _markup = this.markup(document[0], document[1], document[2], document[3],
                              document[4], document[5] );
    table.find('tbody').append( _markup );

  }


  _image_markup( type ){
    if( type == 'Video' ){ return '<i class="fas fa-video" style="padding-right:8px"></i> Video' }
    if( type == 'Powerpoint' ){ return '<i class="fas fa-file-powerpoint" style="padding-right:10px"></i> PDF' }
    if( type == 'PDF' ){ return '<i class="fas fa-file-pdf" style="padding-right:10px"></i> PPTx' }
    if( type == 'Link' ){ return '<i class="fas fa-link" style="padding-right:10px"></i> Link' }
    if( type == 'Template' ){ return '<i class="fas fa-file-download" style="padding-right:10px"></i> Template' }
    return ''
  }

  _color( type ){
    //returns the badge color based on the specified type
    if( type == 'Video' ){ return 'btn-primary' }
    if( type == 'Powerpoint' ){ return 'btn-warning' }
    if( type == 'PDF' ){ return 'btn-danger' }
    if( type == 'Link' ){ return 'btn-info' }
    if( type == 'Template' ){ return 'btn-success' }
    return 'btn-default'

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


  markup( id, type, user, link, date, name ){

    var image_markup = this._image_markup( type)
    var color = this._color( type )
    var padding = this._padding( type )

    var button_markup = ` <a  class="btn btn-primary btn-round ${color}"
                              onclick="element_modal_html_class.view(${id})"
                              role="button" href="${link}">
                          ${image_markup}
                        </a>
                        `
    if ( date != null ){ var datestring = date.toString().split('T')[0]; }

    return   `
            <tr id=${id}>
              <td id='type'>${button_markup}</td>
              <td id='name'>${name} </td>
              <th id='user'>${user} </th>
            </tr>
            `

  }


  view( id ){
    // adds a view object for the selected object

    $.ajax({
        url: url_prefix() + '/ajax/views/document/view',
        data: { 'id' : id,
                },
        success: function (data) {
        },
        error: function(data) {
            $("#MESSAGE-DIV").html("Something went wrong!");
        }
    });
    return false;

  };


}
