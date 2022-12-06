<template>
  <div class="home">
    <div class="rotated-div d-none d-lg-block bg-red"></div>
    <div class="top-5 row position-absolute h-100 w-100 text-light">
      <div class="col-5 d-none d-lg-block info-img "></div>
      <div class="col-lg-7 d-flex flex-column align-items-center justify-content-center home">
        <div class="info-text d-lg-block d-flex flex-column align-items-center">
          <div class="d-lg-none info-img-sm my-3"></div>
          <h1 class="text-red text-center text-lg-start"><span class="d-none  d-xl-inline">-</span> <span class="ms-xl-3">I' M ILGAR HASANZADA.</span></h1>
          <h1 class="ms-xl-5 text-center text-lg-start">WEB DEVELOPER</h1>
          <p class="mt-3 mx-5 mx-lg-0 text-center text-lg-start description">Lorem ipsum, dolor sit amet consectetur adipisicing elit. Natus perspiciatis repudiandae aliquam eius hic laboriosam odit, officia officiis quo facilis Lorem ipsum dolor sit amet consectetur, adipisicing elit. Dicta, commodi!</p>
          <button class="my-btn p-0 ps-3 py btn bg-outline-red text-light rounded-5"><span class="pe-4">MORE ABOUT ME</span><svg xmlns="http://www.w3.org/2000/svg" fill="var(--my-red)" width="50" height="50" viewBox="0 0 24 24"><path d="M12 0c-6.627 0-12 5.373-12 12s5.373 12 12 12 12-5.373 12-12-5.373-12-12-12zm1 17v-4h-8v-2h8v-4l6 5-6 5z"/></svg></button>
        </div>
      </div>
    </div>
  </div>
</template>

<style>
.home{
  padding-bottom: 100px;
}
.rotated-div{
  left: -76%;
  position: fixed;
  transform: rotate(-15deg);
  width: 100%;
  height: 200%;
  z-index: 5;
}
.info-img{
  background-repeat: no-repeat;
  background-size: cover;
  background-position: top;
  /* position: absolute; */
  height:90%;
  width: 33%;
  background-image: url("/home/ilgar_hasanzada/Pictures/Screenshot\ from\ 2022-10-01\ 15-58-09.png");
  border-radius: 30px;
  z-index: 11;
  margin-left: 40px;
  box-shadow: 0 0 60px 10px rgb(0 0 0 / 90%);
  
}
.info-img-sm{
  background-repeat: no-repeat;
  background-size: cover;
  background-position: top;
  /* position: absolute; */
  height:230px;
  width: 230px;
  border: 4px solid #252525;
  background-image: url("/home/ilgar_hasanzada/Pictures/Screenshot\ from\ 2022-10-01\ 15-58-09.png");
  border-radius: 100%;
  box-shadow: 0 0 7px rgb(0 0 0 / 90%);
  z-index: 11;
}
.top-5{
  top: 5%;
  /* bottom: 5%; */
}
.info-padding{
  padding: 20%;
}
h1{
  font-size: 50px;
font-weight: bold;
}
.bg-gray{
  background-color: #2b2a2a;
}
button:hover{
  background-color: var(--my-red) !important;
}
button span{
  font-size: 16px;
  vertical-align: middle;
}
.info-text{
  padding-left: 20%;
  padding-right: 40px;
  line-height: 35px;
}
@media screen and (max-width: 991px) {
  .top-5{
left: 10px;
}
  h1{
    font-size: 35px;
  }
  .info-text{
  padding: 0px;
}
.description{
  font-size: 14px;
}}
@media screen and (min-width: 992px) and (max-width: 1200px) {
  .d-my-none{
    display: none;
  }
 
.info-text{
  padding: 10%;
}
h1{
  font-size: 40px;

}
  }
  
</style>