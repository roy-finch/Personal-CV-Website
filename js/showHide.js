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

function show(id) {
    var item = document.getElementById(id);
    
    item.style.display = "display";
}

function hide(id) {
    var item = document.getElementById(id);

    item.style.display = "none";
}

function setAttr(id, attr, value) {
    var item = document.getElementById(id);

    item.setAttribute(attr, value);
}

function getAttr(id, attr) {
    var item = document.getElementById(id);

    return item.getAttribute(attr);
}