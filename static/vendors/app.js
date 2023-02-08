let sidebar = document.querySelector(".sidebar");
let sidebarBtn = document.querySelector(".sidebarBtn");
sidebarBtn.onclick = function() {
    sidebar.classList.toggle("active");
    if (sidebar.classList.contains("active")) {
        sidebarBtn.classList.replace("bx-menu", "bx-menu-alt-right");
    } else sidebarBtn.classList.replace("bx-menu-alt-right", "bx-menu");
};

$(document).ready(function() {
    $("#kebeletable").DataTable();
    $("#addresstable").DataTable();
    $("#housetable").DataTable();
    $("#familytable").DataTable();
    $("#idcardtable").DataTable();
    $("#employeetable").DataTable();
    $("#lbtable").DataTable();
    $("#lbotable").DataTable();
    $("#certificatetable").DataTable();
    

 
});
const printedpart =document.querySelector('.printed-part')
console.log(printedpart)

const btn = document.getElementById('printbtn')
btn.addEventListener('click' ,Print)

const bodyContent = document.querySelector('.body-content')
const nav = document.querySelector('.removedNav')

const navContent = document.querySelector('.nav-content')
console.log(nav)
function Print(){
     nav.removeChild(navContent)
     bodyContent.removeChild(sidebar)
    printedpart.removeChild(btn)
    window.print()
}
