<template>
    <div class="text-light">
      <nav class="d-md-flex h-100 position-absolute d-none">
        <!-- <svg @click="show_navbar()" class="cursor-pointer z-index-10 fixed-top my-3 ms-3" fill="white" height="50"  clip-rule="evenodd" fill-rule="evenodd" stroke-linejoin="round" stroke-miterlimit="2" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="m22 16.75c0-.414-.336-.75-.75-.75h-18.5c-.414 0-.75.336-.75.75s.336.75.75.75h18.5c.414 0 .75-.336.75-.75zm0-5c0-.414-.336-.75-.75-.75h-18.5c-.414 0-.75.336-.75.75s.336.75.75.75h18.5c.414 0 .75-.336.75-.75zm0-5c0-.414-.336-.75-.75-.75h-18.5c-.414 0-.75.336-.75.75s.336.75.75.75h18.5c.414 0 .75-.336.75-.75z" fill-rule="nonzero"/></svg> -->
        <div class="bg-dark dash-nav z-index-20" id="dash-nav"> 
            <div class="mt-3 d-flex justify-content-end me-3">
                <svg id="nav-icon1" @click="show_navbar()" class="cursor-pointer" fill="white" height="50" clip-rule="evenodd" fill-rule="evenodd" stroke-linejoin="round" stroke-miterlimit="2" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="m11 16.745c0-.414.336-.75.75-.75h9.5c.414 0 .75.336.75.75s-.336.75-.75.75h-9.5c-.414 0-.75-.336-.75-.75zm-9-5c0-.414.336-.75.75-.75h18.5c.414 0 .75.336.75.75s-.336.75-.75.75h-18.5c-.414 0-.75-.336-.75-.75zm4-5c0-.414.336-.75.75-.75h14.5c.414 0 .75.336.75.75s-.336.75-.75.75h-14.5c-.414 0-.75-.336-.75-.75z" fill-rule="nonzero"/></svg>
                <svg id="nav-icon2" @click="show_navbar()" class="cursor-pointer d-none" fill="white" height="50"  clip-rule="evenodd" fill-rule="evenodd" stroke-linejoin="round" stroke-miterlimit="2" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="m22 16.75c0-.414-.336-.75-.75-.75h-18.5c-.414 0-.75.336-.75.75s.336.75.75.75h18.5c.414 0 .75-.336.75-.75zm0-5c0-.414-.336-.75-.75-.75h-18.5c-.414 0-.75.336-.75.75s.336.75.75.75h18.5c.414 0 .75-.336.75-.75zm0-5c0-.414-.336-.75-.75-.75h-18.5c-.414 0-.75.336-.75.75s.336.75.75.75h18.5c.414 0 .75-.336.75-.75z" fill-rule="nonzero"/></svg>
            </div>
            <div class="main-navbar" id="main-navbar">
                <router-link to="/admin/resume" class="d-flex dash-nav-item nav-link my-3"><div class="nav-item-start"></div><span class="bg-black dash-icon p-2 rounded-circle me-1 ms-3"><svg xmlns="http://www.w3.org/2000/svg" fill="white" width="24" height="18" viewBox="0 0 24 24"><path d="M19 7.001c0 3.865-3.134 7-7 7s-7-3.135-7-7c0-3.867 3.134-7.001 7-7.001s7 3.134 7 7.001zm-1.598 7.18c-1.506 1.137-3.374 1.82-5.402 1.82-2.03 0-3.899-.685-5.407-1.822-4.072 1.793-6.593 7.376-6.593 9.821h24c0-2.423-2.6-8.006-6.598-9.819z"/></svg></span><span>Resume</span></router-link>
                <router-link to="/admin/portfolios" class="d-flex dash-nav-item nav-link my-3"><div class="nav-item-start"></div><span class="bg-black dash-icon p-2 rounded-circle me-1 ms-3"><svg xmlns="http://www.w3.org/2000/svg" fill="white" width="24" height="18" viewBox="0 0 24 24"><path d="M12.23 15.5c-6.801 0-10.367-1.221-12.23-2.597v9.097h24v-8.949c-3.218 2.221-9.422 2.449-11.77 2.449zm1.77 2.532c0 1.087-.896 1.968-2 1.968s-2-.881-2-1.968v-1.032h4v1.032zm-14-8.541v-2.491h24v2.605c0 5.289-24 5.133-24-.114zm9-7.491c-1.104 0-2 .896-2 2v2h2v-1.5c0-.276.224-.5.5-.5h5c.276 0 .5.224.5.5v1.5h2v-2c0-1.104-.896-2-2-2h-6z"/></svg></span><span>Portfolios</span></router-link>
                <router-link to="/admin/blogs" class="d-flex dash-nav-item nav-link my-3"><div class="nav-item-start"></div><span class="bg-black dash-icon p-2 rounded-circle me-1 ms-3"><svg xmlns="http://www.w3.org/2000/svg" fill="white" width="24" height="20" viewBox="0 0 24 24"><path d="M19.619 21.671c-5.038 1.227-8.711-1.861-8.711-5.167 0-3.175 3.11-5.467 6.546-5.467 3.457 0 6.546 2.309 6.546 5.467 0 1.12-.403 2.22-1.117 3.073-.029 1 .558 2.435 1.088 3.479-1.419-.257-3.438-.824-4.352-1.385zm-10.711-5.167c0-4.117 3.834-7.467 8.546-7.467.886 0 1.74.119 2.544.338-.021-4.834-4.761-8.319-9.998-8.319-5.281 0-10 3.527-10 8.352 0 1.71.615 3.391 1.705 4.695.047 1.527-.851 3.718-1.661 5.313 2.168-.391 5.252-1.258 6.649-2.115.803.196 1.576.304 2.328.363-.067-.379-.113-.765-.113-1.16z"/></svg></span><span>Blogs</span></router-link>
                <router-link to="/admin/messages" class="d-flex dash-nav-item nav-link my-3"><div class="nav-item-start"></div><span class="bg-black dash-icon p-2 rounded-circle me-1 ms-3"><svg xmlns="http://www.w3.org/2000/svg" fill="white" width="24" height="18" viewBox="0 0 24 24"><path d="M.026 24l11.974-11.607 11.974 11.607h-23.948zm11.964-23.961l-11.99 8.725v12.476l7.352-7.127-5.653-4.113 10.291-7.488 10.309 7.488-5.655 4.108 7.356 7.132v-12.476l-12.01-8.725z"/></svg></span><span>Messages</span></router-link>
            </div>
        </div>
      </nav>
      <nav class="d-md-none h-100 position-absolute d-flex">
        <svg @click="show_navbar()" class="z-index-10 cursor-pointer fixed-top my-3 ms-3" fill="white" height="50"  clip-rule="evenodd" fill-rule="evenodd" stroke-linejoin="round" stroke-miterlimit="2" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="m22 16.75c0-.414-.336-.75-.75-.75h-18.5c-.414 0-.75.336-.75.75s.336.75.75.75h18.5c.414 0 .75-.336.75-.75zm0-5c0-.414-.336-.75-.75-.75h-18.5c-.414 0-.75.336-.75.75s.336.75.75.75h18.5c.414 0 .75-.336.75-.75zm0-5c0-.414-.336-.75-.75-.75h-18.5c-.414 0-.75.336-.75.75s.336.75.75.75h18.5c.414 0 .75-.336.75-.75z" fill-rule="nonzero"/></svg>
        <div @dragleave ="show_navbar()" class="bg-dark z-index-20 dash-nav1" id="dash-nav1">
          <div class="mt-3 d-flex justify-content-end me-3">
            <svg @click="show_navbar()" class="cursor-pointer" fill="white" height="50" clip-rule="evenodd" fill-rule="evenodd" stroke-linejoin="round" stroke-miterlimit="2" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="m11 16.745c0-.414.336-.75.75-.75h9.5c.414 0 .75.336.75.75s-.336.75-.75.75h-9.5c-.414 0-.75-.336-.75-.75zm-9-5c0-.414.336-.75.75-.75h18.5c.414 0 .75.336.75.75s-.336.75-.75.75h-18.5c-.414 0-.75-.336-.75-.75zm4-5c0-.414.336-.75.75-.75h14.5c.414 0 .75.336.75.75s-.336.75-.75.75h-14.5c-.414 0-.75-.336-.75-.75z" fill-rule="nonzero"/></svg>
          </div>
          <router-link to="/admin/resume" class="d-flex dash-nav-item nav-link my-3"><div class="nav-item-start"></div><span class="bg-black dash-icon p-2 rounded-circle me-1 ms-3"><svg xmlns="http://www.w3.org/2000/svg" fill="white" width="24" height="18" viewBox="0 0 24 24"><path d="M19 7.001c0 3.865-3.134 7-7 7s-7-3.135-7-7c0-3.867 3.134-7.001 7-7.001s7 3.134 7 7.001zm-1.598 7.18c-1.506 1.137-3.374 1.82-5.402 1.82-2.03 0-3.899-.685-5.407-1.822-4.072 1.793-6.593 7.376-6.593 9.821h24c0-2.423-2.6-8.006-6.598-9.819z"/></svg></span><span>Resume</span></router-link>
          <router-link to="/admin/portfolios" class="d-flex dash-nav-item nav-link my-3"><div class="nav-item-start"></div><span class="bg-black dash-icon p-2 rounded-circle me-1 ms-3"><svg xmlns="http://www.w3.org/2000/svg" fill="white" width="24" height="18" viewBox="0 0 24 24"><path d="M12.23 15.5c-6.801 0-10.367-1.221-12.23-2.597v9.097h24v-8.949c-3.218 2.221-9.422 2.449-11.77 2.449zm1.77 2.532c0 1.087-.896 1.968-2 1.968s-2-.881-2-1.968v-1.032h4v1.032zm-14-8.541v-2.491h24v2.605c0 5.289-24 5.133-24-.114zm9-7.491c-1.104 0-2 .896-2 2v2h2v-1.5c0-.276.224-.5.5-.5h5c.276 0 .5.224.5.5v1.5h2v-2c0-1.104-.896-2-2-2h-6z"/></svg></span><span>Portfolios</span></router-link>
          <router-link to="/admin/blogs" class="d-flex dash-nav-item nav-link my-3"><div class="nav-item-start"></div><span class="bg-black dash-icon p-2 rounded-circle me-1 ms-3"><svg xmlns="http://www.w3.org/2000/svg" fill="white" width="24" height="20" viewBox="0 0 24 24"><path d="M19.619 21.671c-5.038 1.227-8.711-1.861-8.711-5.167 0-3.175 3.11-5.467 6.546-5.467 3.457 0 6.546 2.309 6.546 5.467 0 1.12-.403 2.22-1.117 3.073-.029 1 .558 2.435 1.088 3.479-1.419-.257-3.438-.824-4.352-1.385zm-10.711-5.167c0-4.117 3.834-7.467 8.546-7.467.886 0 1.74.119 2.544.338-.021-4.834-4.761-8.319-9.998-8.319-5.281 0-10 3.527-10 8.352 0 1.71.615 3.391 1.705 4.695.047 1.527-.851 3.718-1.661 5.313 2.168-.391 5.252-1.258 6.649-2.115.803.196 1.576.304 2.328.363-.067-.379-.113-.765-.113-1.16z"/></svg></span><span>Blogs</span></router-link>
          <router-link to="/admin/messages" class="d-flex dash-nav-item nav-link my-3"><div class="nav-item-start"></div><span class="bg-black dash-icon p-2 rounded-circle me-1 ms-3"><svg xmlns="http://www.w3.org/2000/svg" fill="white" width="24" height="18" viewBox="0 0 24 24"><path d="M.026 24l11.974-11.607 11.974 11.607h-23.948zm11.964-23.961l-11.99 8.725v12.476l7.352-7.127-5.653-4.113 10.291-7.488 10.309 7.488-5.655 4.108 7.356 7.132v-12.476l-12.01-8.725z"/></svg></span><span>Messages</span></router-link>
        </div>
      </nav>
      <!-- <div class="ms-250" id="my-container">
        <div class="container-fluid">
          <div class="row" style="height:100vh;">
            <div class="col col-12 col-md-6 bg-warning">salam</div>
            <div class="col col-12 col-md-6 bg-yellow">salam</div>
            <div class="col col-12 col-md-6 bg-yellow">salam</div>
            <div class="col col-12 col-md-6 bg-warning">salam</div>
          </div>
        </div>
      </div> -->
      
    </div>
  </template>
  
  <script>
  export default {
    name:"NavbarView",
    methods:{
      show_navbar(){
        document.getElementById("dash-nav").classList.toggle("dash-nav-500")
        document.getElementById("dash-nav1").classList.toggle("dash-nav1-500")
        document.getElementById("nav-icon1").classList.toggle("d-none")
        document.getElementById("nav-icon2").classList.toggle("d-none")
        document.getElementById("main-navbar").classList.toggle("d-none")
        document.getElementById("admin-pages").classList.toggle("ms-250")
        document.getElementById("admin-pages").classList.toggle("ms-20")
      }
    }
    
  }
  </script>
  
  <style>
    .z-index-10{
      z-index: 1;
    }
    .z-index-20{
      z-index: 10;
    }
    .dash-nav-500{
      left: -170px !important;
    }
    .dash-nav1-500{
      left: 0px !important;
    }
    .dash-nav1{
      left: -251px;
      position: fixed;
      height: 100%;
      transition: 1s;
      width: 250px !important;
     }
     .dash-nav{
      left: 0;
      position: fixed;
      height: 100%;
      transition: 1s;
      width: 250px !important;
     }
      .dash-nav-item{
      width: 85%!important;
      border-radius: 0 25px 25px 0;
      height: 50px;
      align-items: center;
     }
     .dash-nav-item:hover{
      background: var(--my-black);
      color: var(--my-red);
     }
     .dash-nav-item:hover svg{
      fill: var(--my-red);
     }
     .dash-nav-item:hover .dash-icon{
      background:  rgb(33, 37, 41)!important;
     }
      .dash-nav-item:hover .nav-item-start{
        background: var(--my-red); 
    }
     .nav-item-start{
      width: 4px !important;
      height: 100% !important;
     }
     .dash-nav *, .dash-nav1 *{
      transition: .1s !important;
     }
     .dash-nav a.router-link-exact-active,.dash-nav1 a.router-link-exact-active{
        background: var(--my-black);
        color: var(--my-red);
    }
    .dash-nav a.router-link-exact-active svg,.dash-nav1 a.router-link-exact-active svg{
        fill: var(--my-red);
    }
    .dash-nav a.router-link-exact-active .dash-icon,.dash-nav1 a.router-link-exact-active .dash-icon{
      background:  rgb(33, 37, 41)!important;
     }
     .dash-nav a.router-link-exact-active  .nav-item-start,.dash-nav1 a.router-link-exact-active  .nav-item-start{
        background: var(--my-red); 
    }
  </style>