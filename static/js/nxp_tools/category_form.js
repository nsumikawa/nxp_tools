/*
Category.js
=======

description
-----------
Routines for manipulating and rendering the category form

Author : Nik Sumikawa
Date : Feb 13, 2019

*/

var category_form_class
var category_html_class

class category_form {

  constructor( modal, form, form_name, elements_div ){
    this.modal = modal;
    this.form = form;
    this.form_name = form_name;
    this.elements_div = elements_div
    this.category_id = 'None';
  }

  new(){

    //clear the category id
    this.category_id = 'None'

    //clear the form content
    this.form.elements.type.value = ''
    this.form.elements.tool.value = ''
    this.form.elements.name.value = ''
    this.form.elements.description.value = ''

    //hide the elements block as there will be no previously existing elements
    document.getElementById(this.elements_div + '_container').style.display='none'

    document.getElementById(this.modal).style.display='Block'
  }

  push( ){
    // populates and shows the  modal with all events corresponding to the product

    // add the category id to the form
    $('<input>').attr({
        type: 'hidden',
        name: 'id',
        value: this.category_id
    }).appendTo( '#' + this.form_name );

    var self = this;

    //ajax request to push content to the database.
    $.ajax({
        type: $( '#' + this.form_name ).attr('method'),
        url: url_prefix() + '/ajax/views/category/push',
        data: $( '#' + this.form_name ).serialize(),
        success: function (data) {
            //update the current page on return

            if( self.category_id == 'None' ){
              // add a new entry when one does not exist
              category_html_class.add( data.id, data.name, data.description )

            } else {
              //replace the existing contents
              category_html_class.replace( data.id, data.name, data.description )
            }
            // $('#category_' + data.id ).remove()

            // $('#id_goal').append( $("<option></option>")
            //                       .attr("value",key)
            //                       .text(form_field[key]));
            //
            document.getElementById(category_form_class.modal).style.display='None'
        },
        error: function(data) {
            $("#MESSAGE-DIV").html("Something went wrong!");
        }
    });
    return false;

  };

  pull( category_id ){
    // populates and shows the  modal with all events corresponding to the product

    // set the global value for the category id
    this.category_id = category_id


    //ajax request to push content to the database.
    $.ajax({
        url: url_prefix() + '/ajax/views/category/pull',
        data: {'id':category_id},
        success: function (data) {
            //update the form content
            category_form_class.form.elements.type.value = data.type
            category_form_class.form.elements.tool.value = data.tool
            category_form_class.form.elements.name.value = data.name
            category_form_class.form.elements.description.value = data.description

            //hide the elements block as there will be no previously existing elements
            document.getElementById(category_form_class.elements_div + '_container').style.display='Block'

            //clear the div then add elements to it belonging to the category
            document.getElementById(category_form_class.elements_div).innerHTML = ""
            category_form_class.populate_element_div( data.elements );

            document.getElementById(category_form_class.modal).style.display='Block'

        },
        error: function(data) {
            $("#MESSAGE-DIV").html("Something went wrong!");
        }
    });
    return false;

  };

  delete( ){
    // populates and shows the  modal with all events corresponding to the product

    $('#category_' + this.category_id ).remove()

    document.getElementById(category_form_class.modal).style.display='None'

    //ajax request to push content to the database.
    $.ajax({
        url: url_prefix() + '/ajax/views/category/delete',
        data: {'id':this.category_id},
        success: function (data) {
          //TODO remove contents from the page
          document.getElementById(category_form_class.modal).style.display='None'
        },
        error: function(data) {
            $("#MESSAGE-DIV").html("Something went wrong!");
        }
    });
    return false;

  };

  add_element( ){
    // opens the element modal to allwo for the addition of anew element
    element_form_class.new( this.category_id )
  }

  populate_element_div( data ){
    // add elements to the element block in the category form
    for (var i = 0; i < data.length; i++) {
      var _markup = element_html_class.markup(data[i][0], data[i][1], data[i][2],
                                              `category_element_${data[i][0]}` );

      document.getElementById(category_form_class.elements_div).innerHTML += _markup
    }
  }

}






class category_html {

  constructor( parent_str, tool, type, user_status ){
    // this.parent = parent; //$("#product_id")
    this.parent = $('#' + parent_str )
    this.parent_str = parent_str
    this.tool = tool;
    this.type = type;
    this.max_columns = 2
    this.col_number = 0;

    this.user_status = user_status;
  }

  page( ){
    // populates the entire page with categories

    var self = this

    //ajax request to push content to the database.
    $.ajax({
        url: url_prefix() + '/ajax/views/category/get',
        data: { 'tool':category_html_class.tool,
                'type':category_html_class.type,
                },
        success: function (data) {

          //clear the parent before adding categories
          self.parent.html("");
          // $('#category_root').html("");

          //add the categories
          for (var i = 0; i < data.categories.length; i++) {
            self.add( data.categories[i][0], data.categories[i][1], data.categories[i][2]);
          }

          element_html_class.page()
        },
        error: function(data) {
            $("#MESSAGE-DIV").html("Something went wrong!");
        }
    });
    return false;

  };

  add( id, name, description ){
    //adds a single item to the parent

    if( (this.col_number%this.max_columns) == 0 ){
      //create a new col when the adding an element that exceeds the maximum number of columns
      document.getElementById(this.parent_str).innerHTML += this.markup( id, name, description )

    }else{
      //append the existing row witha  new entry
      var row_number = Math.floor(this.col_number/2)
      document.getElementById(`row_number_${row_number}`).innerHTML += this.markup_body( id, name, description )

    }

    //advance the number of columns
    this.col_number += 1
    // $('#category_root').appendChild(_markup);
  }

  replace( id, name, description ){
    //replaces the html in the specified block
    document.getElementById(`category_title_name_${id}`).innerHTML = name
  }

  markup_add_button( id ){
    // returns the markup for adding a button. this allows for controll based on user availability

    var _markup = ''
    if( this.user_status == true){
      _markup = `
                <div class="col" align='right' style='max-width:100px'>
                      <span class="badge badge-pill badge-success"
                      onclick="category_form_class.pull(${id})">
                    Edit<i class="fa fa-edit" style="padding-left:10px"></i>
                  </span>
                </div>
              `
    }

    return _markup;

  }

  markup_body( id, name, description ){
    var _markup = `
                  <div class="col"  id='category_${id}'>
                    <div class="card ">

                      <div class="card-header ">
                        <div class="row">
                          <div class="col">
                            <h6 class="card-category" data-toggle="tooltip" data-placement="right"
                                data-boundary=""
                                title="${description}" id='category_title_name_${id}'>
                                ${name}
                            </h6>
                          </div>
                          <div class="col" align='right' >
                            ${this.markup_add_button(id)}
                          </div>
                        </div>
                      </div>

                      <div class="card-body" id='body_${id}'>
                      </div>

                    </div>
                  </div>
                  `

    return _markup;
  }

  markup( id, name, description ){
    // populates and shows the  modal with all events corresponding to the product

    var row_number = Math.floor(this.col_number/2)

    var _markup = `
                  <div class="row" id="row_number_${row_number}">
                    ${this.markup_body( id, name, description )}
                  </div>
                  `
    return _markup;

  };


}
