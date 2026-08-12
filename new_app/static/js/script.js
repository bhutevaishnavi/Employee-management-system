document.addEventListener("DOMContentLoaded", function(){

    const menuBtn = document.querySelector(".navbar-toggler");
    const sidebar = document.querySelector(".sidebar");

    if(menuBtn && sidebar){

        menuBtn.addEventListener("click", function(){

            sidebar.classList.toggle("active");

        });

    }

});