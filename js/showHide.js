function showHide(id) {
    var item = document.getElementById(id);
    var button = document.getElementById(id+"btn");

    if (button.getAttribute("val") == "false") {
        item.style.display = "none";
        button.setAttribute("val", "true");
    } else {
        item.style.display = "block";
        button.setAttribute("val", "false");
    }
}