/*
Element.js
=======

description
-----------
Routines for manipulating and rendering the element page

Author : Nik Sumikawa
Date : Feb 13, 2019

*/


var element_form_class
var element_html_class


class element_form {

  constructor( modal, form, form_name, document_div ){
    this.modal = modal;
    this.form = form;
    this.form_name = form_name;
    this.document_div = document_div;
    this.element_id = 'None';
  }

  new( category = ''){
    //clears the contents of the html form

    //clear the element id
    this.element_id = 'None'

    //clear the form content
    this.form.elements.category.value = category
    this.form.elements.name.value = ''
    this.form.elements.description.value = ''

    document_html_class.hide()
    // document.getElementById(this.document_div + '_container').style.display='None'
    document.getElementById(this.modal).style.display='Block'
  }

  push( ){
    // populates and shows the  modal with all events corresponding to the product

    var self = this

    // add the element id to the form
    $('<input>').attr({
        type: 'hidden',
        name: 'id',
        value: this.element_id
    }).appendTo( '#' + this.form_name );

    //ajax request to push content to the database.
    $.ajax({
        type: $( '#' + this.form_name ).attr('method'),
        url: url_prefix() + '/ajax/views/element/push',
        data: $( '#' + this.form_name ).serialize(),
        success: function (data) {
            //update the current page on return

            if( self.element_id == 'None' ){
              element_html_class.add( data.category_id, data.id, data.name, data.description )
            } else {
              element_html_class.replace( data.id, data.name, data.description )
            }

            category_form_class.populate_element_div( [[data.id, data.name, data.description]] )

            document.getElementById(element_form_class.modal).style.display='None'
        },
        error: function(data) {
            $("#MESSAGE-DIV").html("Something went wrong!");
        }
    });
    return false;

  };

  pull( element_id ){
    // populates and shows the  modal with all events corresponding to the product

    // set the global value for the element id
    this.element_id = element_id


    //ajax request to push content to the database.
    $.ajax({
        url: url_prefix() + '/ajax/views/element/pull',
        data: {'id':element_id},
        success: function (data) {
            //update the form content
            element_form_class.form.elements.category.value = data.category
            element_form_class.form.elements.name.value = data.name
            element_form_class.form.elements.description.value = data.description

            //clear the div then add elements to it belonging to the category
            document_html_class.clear()
            document_html_class.add_multiple( data.document)
            document_html_class.show()

            // document.getElementById(element_form_class.document_div + '_container').style.display='Block'
            // document.getElementById(element_form_class.document_div).innerHTML = ""
            // element_form_class.populate_document_div( data.document );


            document.getElementById(element_form_class.modal).style.display='Block'
        },
        error: function(data) {
            $("#MESSAGE-DIV").html("Something went wrong!");
        }
    });
    return false;

  };

  delete( ){
    // populates and shows the  modal with all events corresponding to the product

    $('#element_' + this.element_id ).remove()

    document.getElementById(element_form_class.modal).style.display='None'

    //ajax request to push content to the database.
    $.ajax({
        url: url_prefix() + '/ajax/views/element/delete',
        data: {'id':this.element_id},
        success: function (data) {
          //TODO remove contents from the page
          document.getElementById(element_form_class.modal).style.display='None'
        },
        error: function(data) {
            $("#MESSAGE-DIV").html("Something went wrong!");
        }
    });
    return false;

  };

  add_document( ){
    // opens the element modal to allwo for the addition of anew element
    document_form_class.new( this.element_id )
  }


}



class element_html {

  constructor( tool, type, user_status ){
    // this.parent = parent; //$("#product_id")
    this.tool = tool;
    this.type = type;
    this.user_status = user_status;
  }

  page( ){
    // populates the entire page with categories

    var self = this

    //ajax request to push content to the database.
    $.ajax({
        url: url_prefix() + '/ajax/views/element/get',
        data: { 'tool':category_html_class.tool,
                'type':category_html_class.type,
                },
        success: function (data) {

          //add the categories
          for (var i = 0; i < data.elements.length; i++) {
            self.add( data.elements[i][0], data.elements[i][1],
                      data.elements[i][2], data.elements[i][3]);
          }

        },
        error: function(data) {
            $("#MESSAGE-DIV").html("Something went wrong!");
        }
    });
    return false;

  };

  add( category_id, id, name, description, element='None', markup_element='None' ){
    //adds a single item to the parent

    if(element == 'None'){ element = `body_${category_id}`}

    //do not add markup when the element does not exist
    if( document.getElementById(element) == null){ return }

    document.getElementById(element).innerHTML += this.markup( id, name, description, markup_element )

  }

  replace( id, name, description, element='None' ){
    //replaces the html in the specified block

    if(element == 'None'){ element = `element_${id}`}
    document.getElementById(element).innerHTML = `
                                                  ${this.markup_edit_button( id )}
                                                  ${this.markup_info_button( id )}
                                                  ${this.markup_name( name, description )}
                                                  `
  }

  markup_edit_button( id ){
    // returns the markup for adding a button. this allows for controll based on user availability

    //do not return the edit button when the user is not signed in
    if( this.user_status == false ){ return '' }

    return `
            <div class="col" style='width:18px; max-width:18px'>
              <span class="badge badge-pill badge-success"
                    onclick="element_form_class.pull(${id})">
                <i class="fa fa-edit"></i>
              </span>
            </div>
            `
  }

  markup_info_button( id ){
    return  `
            <div class="col" style='width:18px; max-width:18px'>
              <span class="badge badge-pill badge-info"
                    onclick="element_modal_html_class.open(${id})">
                <i class="fa fa-info"></i>
              </span>
            </div>
            `

  }

  markup_name( name, description ){
    return  `
            <div class="col" style='padding-top:3px'>
              <h6 class="card-title" data-toggle="tooltip" data-placement="right"
                  title="${description}">
                  ${name}
              </h6>
            </div>
            `
  }

  markup( id, name, description, element ){
    // populates and shows the  modal with all events corresponding to the product

    if(element == 'None'){ element = `element_${id}`}
    var _markup = `
                  <div class="row" id="${element}">
                    ${this.markup_edit_button( id )}
                    ${this.markup_info_button( id )}
                    ${this.markup_name( name, description )}
                  </div>
                  `
    return _markup;

  };


}
