/*
Search.js
=========

description
-----------
Routiens for searching through the database

Author : Nik Sumikawa
Date : Feb 20, 2019

*/


var search_class

class search {

  constructor( ){
    this._modal
    this._table
  }


  set modal( value ){ this._modal = value}
  get modal(){ return this._modal }

  set table( value ){ this._table = value}
  get table(){ return this._table }

  search( ){
    // populates the modal based on the search field

    //retrieves the contents from the search field
    var search_field = document.getElementById('search_field').value
    console.log( search_field )
    console.log( this._modal )

    var self = this;

    $.ajax({
        url: url_prefix() + '/ajax/views/search/get',
        data: { 'search_field': search_field },
        success: function (data) {
          console.log( 'do i get here')

          //add the categories
          for (var i = 0; i < data.elements.length; i++) {
            console.log(data.elements[i])
            self.add( data.elements[i], self._table);
          }

          document.getElementById(self.modal).style.display='Block'
        },
        error: function(data) {
            $("#MESSAGE-DIV").html("Something went wrong!");
        }
    });

    return false;

  }

  add( data, table ){
    //adds a single item to the document

    var _markup = this.markup(data[3], data[4], data[5], data[0], data[1], data[2] );
    table.find('tbody').append( _markup );

  }

  markup( id, name, description, tool, type, category ){

    var _markup = element_html_class.markup( id, name, description, 'None' )

    return   `
            <tr id=${id}>
              <td id='type'>${_markup}</td>
              <td id='name'>${tool} </td>
              <td id='user'>${type} </td>
              <td id='user'>${category} </td>
            </tr>
            `

  }



}
