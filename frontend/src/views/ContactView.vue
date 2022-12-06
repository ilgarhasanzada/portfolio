<template>
  <div class="contact mb-5 pb-5">
    <!-- About Me -->
    <div class="text-sm-center w-100">
      <h3 class="position-absolute z-index-1 w-100 ps-3 mt-5"><span class="text-light">GET IN</span> <span class="text-yellow">TOUCH</span></h3>
      <h1 class="position-relative z-index-2 w-100 mt-5">CONTACT</h1>
    </div>
    <div style="margin-top:70px" class="container-xl text-light mt-md-3">
      <div class="row w-100">
        <!-- Info -->
        <div class="col col-12 col-lg-4">
          <h3 class="my-3 d-none d-sm-block">DON'T BE SHY !</h3>
          <h4 class="my-3 d-sm-none">DON'T BE SHY !</h4>
          <div><small>Feel free to get in touch with me. I am always open to discussing new projects, creative ideas or opportunities to be part of your visions.</small></div>
          <div class="d-flex my-4">
            <div><svg xmlns="http://www.w3.org/2000/svg" fill="orange" width="35" height="35" viewBox="0 0 24 24"><path d="M12 1c-3.148 0-6 2.553-6 5.702 0 3.148 2.602 6.907 6 12.298 3.398-5.391 6-9.15 6-12.298 0-3.149-2.851-5.702-6-5.702zm0 8c-1.105 0-2-.895-2-2s.895-2 2-2 2 .895 2 2-.895 2-2 2zm8 6h-3.135c-.385.641-.798 1.309-1.232 2h3.131l.5 1h-4.264l-.344.544-.289.456h.558l.858 2h-7.488l.858-2h.479l-.289-.456-.343-.544h-2.042l-1.011-1h2.42c-.435-.691-.848-1.359-1.232-2h-3.135l-4 8h24l-4-8zm-12.794 6h-3.97l1.764-3.528 1.516 1.528h1.549l-.859 2zm8.808-2h3.75l1 2h-3.892l-.858-2z"/></svg></div>
            <div class="mx-3">
              <small class="d-block text-secondary">ADDRESS POINT</small>
              <small class="d-block">123 Stree New York City , United States Of America 750065.</small>
            </div>
          </div>
          <div class="d-flex my-4">
            <div><svg xmlns="http://www.w3.org/2000/svg" fill="orange" width="35" height="35" viewBox="0 0 24 24"><path d="M.026 24l11.974-11.607 11.974 11.607h-23.948zm11.964-23.961l-11.99 8.725v12.476l7.352-7.127-5.653-4.113 10.291-7.488 10.309 7.488-5.655 4.108 7.356 7.132v-12.476l-12.01-8.725z"/></svg></div>
            <div class="mx-3">
              <small class="d-block text-secondary">MAIL ME</small>
              <small class="d-block">ilqarhsnzad@gmail.com</small>
            </div>
          </div>
          <div class="d-flex my-4">
            <div><svg xmlns="http://www.w3.org/2000/svg" fill="orange" width="35" height="35" viewBox="0 0 24 24"><path d="M12 0c-6.627 0-12 5.373-12 12s5.373 12 12 12 12-5.373 12-12-5.373-12-12-12zm3.445 17.827c-3.684 1.684-9.401-9.43-5.8-11.308l1.053-.519 1.746 3.409-1.042.513c-1.095.587 1.185 5.04 2.305 4.497l1.032-.505 1.76 3.397-1.054.516z"/></svg></div>
            <div class="mx-3">
              <small class="d-block text-secondary">CALL ME</small>
              <small class="d-block">+994(55)-858-32-90</small>
            </div>
          </div>
          <div class="d-flex pt-3">
            <!-- <router-link to="https://snipcart.com" target="_blank" v-for="link in links" :key="link" class="bg-icon p-2 rounded-circle me-3" v-html=link.logo></router-link> -->
            <a class="bg-icon p-2 rounded-circle me-3" :href=link.src target="_blank" v-for="link in links" :key="link" v-html=link.logo></a>
          </div>
        </div>
        <!-- Form -->
        <div class="col col-12 col-lg-8 mt-4">
          <div class="row">
            <div class="col col-12 col-md-6 my-4 my-md-0">
              <input type="text" placeholder="YOUR NAME" name="" id="" class="form-control contact-form rounded-pill bg-gray border-0 px-4 py-2 text-light" aria-describedby="helpId">
            </div>
            <div class="col col-12 col-md-6 my-md-0">
              <input type="text" placeholder="YOUR EMAIL" name="" id="" class="form-control contact-form rounded-pill bg-gray border-0 px-4 py-2 text-light" aria-describedby="helpId">
            </div>
          </div>
          <div class="my-4">
            <input type="text" placeholder="YOUR SUBJECT" name="" id="" class="form-control contact-form rounded-pill bg-gray border-0 px-4 py-2 text-light" aria-describedby="helpId">
          </div>
          <div class="my-4">
             <textarea placeholder="YOUR MESSAGE" class="form-control contact-form message bg-gray border-0 px-4 py-2 text-light" name="" id="" rows="7"></textarea>
          </div>
          <button class="my-btn p-0  ps-3 my-3 btn bg-outline-yellow text-light rounded-5"><span class="pe-4">SEND MESSAGE</span><svg xmlns="http://www.w3.org/2000/svg" fill="#ffb400" width="50" height="50" viewBox="0 0 24 24"><path d="M12 0c-6.627 0-12 5.373-12 12s5.373 12 12 12 12-5.373 12-12-5.373-12-12-12zm1 17v-4h-8v-2h8v-4l6 5-6 5z"/></svg></button>
        </div>
      </div>
    </div>
  </div>
</template>
<script>

export default {
  name:"ContactView",
  data(){
    return{
      links:[
        {
          "logo":'<svg xmlns="http://www.w3.org/2000/svg" fill="white" width="24" height="15" viewBox="0 0 24 24"><path d="M21 13v10h-6v-6h-6v6h-6v-10h-3l12-12 12 12h-3zm-1-5.907v-5.093h-3v2.093l3 3z"/></svg>',
          "name":"instagram",
          "src":"https://snipcart.com"
        },
        {
          "logo":'<svg xmlns="http://www.w3.org/2000/svg" fill="white" width="24" height="15" viewBox="0 0 24 24"><path d="M21 13v10h-6v-6h-6v6h-6v-10h-3l12-12 12 12h-3zm-1-5.907v-5.093h-3v2.093l3 3z"/></svg>',
          "name":"instagram",
          "src":"https://snipcart.com"
        }
      ]
    }
  }
}
</script>
<style>

.contact-form:hover{
  background-color: var(--my-gray);
}
.contact-form:focus{
  background-color: var(--my-gray);
}
.message{
  border-radius: 30px !important;
}
@media screen and (min-width:1141px) {
    .contact-length{
        width: 1150px;
    }
    
}
@media screen and (max-width:1140px) {
    .contact-length{
        width: 100%;
    }
}
</style>