function showHide(id) {
    var item = document.getElementById(id);
    var button = document.getElementById(id+"btn");

    if (button.getAttribute("val") == "true") {
        item.style.display = "none";
        button.setAttribute("val", "false");
    } else {
        item.style.display = "block";
        button.setAttribute("val", "true");
    }
}