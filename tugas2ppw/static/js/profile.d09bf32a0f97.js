$(document).ready(function() {
    $('.select-keahlian').selectmenu();
    $('.select-level').selectmenu();
});

const addKeahlian = function() {
    keahlian = $('.skill-baru').val();
    level = $('.level-baru').val();
    console.log(keahlian);
    console.log(level);
    location.href = 'add-keahlian/'+ keahlian + '/' + level + '/';
}

$(".delete-button").on("click", function(e) {
    var uid = $(this).data('id');
    location.href="delete-keahlian/" + uid;
});
