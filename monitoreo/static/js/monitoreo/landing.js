var ProgressBar;

function chart(id, step_fn) {
    var pct = $(id).attr("data-pct")/100;
    var settings = {
        strokeWidth: 2,
        duration: 2000 * pct,
        easing: 'easeInOut',
        text: {
            style: {
                color: '#555',
                position: 'absolute',
                left: '50%',
                top: '50%',
                padding: 0,
                margin: 0,
                'font-size': '200%',
                transform: {
                    prefix: true,
                    value: 'translate(-50%, -50%)'
                }
            }
        }
    };
    settings.step = step_fn ? step_fn : default_value;
    var circle = new ProgressBar.Circle(id, settings);

    // Leo el porcentaje de el campo 'data-pct' del div. Obligatorio!
    circle.animate(pct);
    return circle;
}

window.onload = function() {
    $(".circle-progressbar").each(function() {
        var id = "#" + $(this).attr("id");
        chart(id);
    });
};

function default_value(_, circle) {
    // Setea el texto al valor porcentual del progreso en cada paso
    var value = Math.round(circle.value() * 100);
    if (value === 0) {
      circle.setText('');
    } else {
      circle.setText(value + "%");
    }
}