// Ocultar resultados si se hace clic fuera del input
document.addEventListener("click", function(e) {
    let lista = document.getElementById("resultados");
    let input = document.getElementById("buscar");
    if (!input.contains(e.target) && !lista.contains(e.target)) {
        lista.style.display = "none";
    }
});

// Funciones para song.html
window.onload = function() {
    var iframe = document.getElementById('videoIframe');
    if(iframe) {
        var iframeWidth = iframe.offsetWidth;
        var aspectRatio = 9 / 16; // Relación de aspecto de YouTube
        iframe.style.height = (iframeWidth * aspectRatio) + 'px';
    }
}

document.addEventListener("DOMContentLoaded", function () {
    let original = document.getElementById("lyrics-original");
    let translated = document.getElementById("lyrics-spanish");

    function syncScroll(event) {
        let other = event.target.id === "lyrics-original" ? translated : original;
        other.scrollTop = event.target.scrollTop;
    }
    if(original) {
        original.addEventListener("scroll", syncScroll);
        translated.addEventListener("scroll", syncScroll);
    }
});