//field contents manager for research fields

var limit = 3;
var field = new Object();
field.contents = [];
field.add = function(text){
  this.contents.push(text);
}
field.remove = function(text){
  var i = this.contents.indexOf(text);
  if (i !== -1){
    this.contents.splice(i, 1);
  }
}
field.asString = function(){
  return this.contents.join(', ');
}

//enumerate allowed fields here
var allowedFields = ['Biology and life sciences', 'Ecology and environmental sciences', 'Medicine and health sciences'];

//creating the treeview
$.getJSON('https://cdn.rawgit.com/travs/PLOS-Subject-Area-Explorer/master/plosthes.2014-5.json', function(data){
  for (var i = data.length - 1; i >= 0; i--){
    //start at array end to deal with array resizing
    var subtree = data[i];
    var pos = allowedFields.indexOf(subtree.text[0]);
    if(pos === -1){
      //field not allowed
      data.splice(pos, 1);
    }
  }
  console.log(data);
  $('#fields').after('<div id="tree"></div>');
  $('.fieldsInput').attr('readonly', '');
  $('#tree').treeview({data: data, levels: 1, nodeIcon: 'glyphicon', multiSelect: true, highlightSelected: true});

  //selecting adds to text field
  $('#tree').on('nodeSelected', function(event, node){
    if(field.contents.length === limit){
      //immediately deselect node if at limit
      $('#tree').treeview('unselectNode', [ node.nodeId ]);
    }
    else{
      field.add(node.text[0]);
      $('.fieldsInput').attr('value', field.asString());
    }
  })

  //deselecting removes from text field
  $('#tree').on('nodeUnselected', function(event, node){
    field.remove(String(node.text[0]));
    $('.fieldsInput').attr('value', field.asString());
  })

})

//styling the form a little

$('.ss-form-question').addClass('form-group');

$('.required-message').remove();

$('.error-message').remove();

$('.ss-password-warning').remove();

$('.ss-q-short, .ss-q-long').addClass('pull-right');

$('select').addClass('pull-right');
