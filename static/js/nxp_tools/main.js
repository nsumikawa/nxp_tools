/*
Main.js
=======

description
-----------
Routines for rendering the main page

Author : Nik Sumikawa
Date : Feb 13, 2019

*/


var main_page_class

class main_page{

  constructor( user_status ){

    this.user_status = user_status

    //default the toolkit to point to Exensio Yield Training Documents
    localStorage.setItem("page_tool", 'Exensio Yield');
    localStorage.setItem("page_type", 'Training');

    this.init_page();
  }

  init_page(){
    //initializes or reinitializes the page

    this.tool = localStorage.getItem("page_tool");
    this.type = localStorage.getItem("page_type");

    //set headers and labels on the size bar
    $('#top_navbar_brand').html( this.tool )
    $('#main_title').html( this.type )
    $(`#sidebar_${this.tool.replace(' ', '_').replace('+','')}_${this.type}`).addClass( "active")

    this.init_category_form();
    this.init_document_form();
    this.init_element_form();
    this.init_element_modal();

    category_html_class.page()
  }

  init_category_form(){
    //initialize the category classes
    var c_form = document.forms.category_form;
    var c_form_name = 'category_form'
    var c_elements_div = 'category_form_elements'
    category_form_class = new category_form( 'category_form_modal', c_form, c_form_name, c_elements_div )
    category_html_class = new category_html( 'category_root', this.tool, this.type, this.user_status )
  }

  init_element_form(){
    //initialize the element classes
    var e_form = document.forms.element_form;
    var e_form_name = 'element_form';
    var e_document_div = 'element_form_documents';
    element_form_class = new element_form( 'element_form_modal', e_form, e_form_name, e_document_div );
    element_html_class = new element_html( this.tool, this.type, this.user_status );

  }

  init_document_form(){
    //initialize the document classes
    var d_form = document.forms.document_form;
    var d_form_name = 'document_form'
    document_form_class = new document_form( 'document_form_modal', d_form, d_form_name )
  }

  init_element_modal(){
    element_modal_html_class = new element_modal_html( 'element_modal', $('#document_table') )
  }

  open( tool, type ){

    //remove the active label on the sidebar
    $(`#sidebar_${this.tool.replace(' ', '_').replace('+','')}_${this.type}`).removeClass()

    localStorage.setItem("page_tool", tool);
    localStorage.setItem("page_type", type);

    //initializes the page to the tool/type
    this.init_page()
  }
}
