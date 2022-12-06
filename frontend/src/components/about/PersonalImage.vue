<template>
    <div>
        <h3 class="text-light d-lg-block d-none">PERSONAL INFOS</h3>
        <div class="about_img"></div>
    </div>
</template>
  
  <script>
  export default {
    name: 'PersonalImage',
  }
  </script>
  
  <style>
    .about_img{
    width: 400px;
    height: 300px;
    background-size: cover;
    background-position: top;
    border-radius: 10px;
    background-image: url("/home/ilgar_hasanzada/Pictures/Screenshot\ from\ 2022-10-01\ 15-58-09.png");
}
@media screen and (max-width: 568px) {
    .about_img{
        width: 230px !important;
        height: 230px !important;
        border-radius: 100%;
        margin-bottom: 50px;
        border: 4px solid #252525;
    }
}
</style>