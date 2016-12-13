var main = function(){
    $('#input-limit').on('change', function(){
        var val = $('#input-limit option:selected').text();
        $('#input-limit option').eq(val).prop('selected', true);

        });

};
$(document).ready(main);