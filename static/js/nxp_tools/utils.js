/*
Stacked Events
==============

Description
-----------
Routines for analyzing the stacked events for a given product

Author : Nik Sumikawa
Date : Feb 1, 2019
*/

function url_prefix(){
  // returns a prefix to add to the url string depending on the host of the get_wsgi_application

  //determine the url location based on the window origin
  if ( window.location.origin == 'http://az84cqc01' ){
    return '/excursion'

  }else{
    return ''

  }
}

function error_alert(){
  //posts a standard alert when an error occurred in the backend

  Swal({
    position: 'top-end',
    type: 'error',
    title: 'An error occurred. We logged the error and will address it ASAP',
    showConfirmButton: true,
    timer: 5000
  })

}


$(function () {
  $('[data-toggle="tooltip"]').tooltip()
})
