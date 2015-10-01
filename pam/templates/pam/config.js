{% load staticfiles %}
config = new function() {
  this.bgcolor = "white";
  this.image =  "{% static 'oxhack.png' %}";
  this.buttonColor = "black";
  this.buttonShow = false;
  this.scannerDownloadLink = "";
}
