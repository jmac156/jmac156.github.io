/*

   HTML AND CSS FINAL PROJECT

   Author: Peter Cler
   Date:   01/19/16

*/

window.onload = setForm;

function setForm() {
   document.forms[0].onsubmit = function() {
      if (this.checkValidity()) alert("No invalid data detected. Will retain data for further testing.");
      return false;
   }
}
