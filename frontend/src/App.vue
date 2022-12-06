<template>
  <nav>
    <div v-if="window.width<=991" class="position-fixed bg-gray fixed-bottom d-flex justify-content-around py-2">
      <router-link to="/" class="nav-link"><div class="bg-icon p-2 rounded-circle"><svg xmlns="http://www.w3.org/2000/svg" fill="white" width="24" height="15" viewBox="0 0 24 24"><path d="M21 13v10h-6v-6h-6v6h-6v-10h-3l12-12 12 12h-3zm-1-5.907v-5.093h-3v2.093l3 3z"/></svg></div></router-link> 
      <router-link to="/about" class="nav-link"><div class="bg-icon p-2 rounded-circle"><svg xmlns="http://www.w3.org/2000/svg" fill="white" width="24" height="15" viewBox="0 0 24 24"><path d="M19 7.001c0 3.865-3.134 7-7 7s-7-3.135-7-7c0-3.867 3.134-7.001 7-7.001s7 3.134 7 7.001zm-1.598 7.18c-1.506 1.137-3.374 1.82-5.402 1.82-2.03 0-3.899-.685-5.407-1.822-4.072 1.793-6.593 7.376-6.593 9.821h24c0-2.423-2.6-8.006-6.598-9.819z"/></svg></div></router-link> 
      <router-link to="/portfolio" class="nav-link"><div class="bg-icon p-2 rounded-circle"><svg xmlns="http://www.w3.org/2000/svg" fill="white" width="24" height="18" viewBox="0 0 24 24"><path d="M12.23 15.5c-6.801 0-10.367-1.221-12.23-2.597v9.097h24v-8.949c-3.218 2.221-9.422 2.449-11.77 2.449zm1.77 2.532c0 1.087-.896 1.968-2 1.968s-2-.881-2-1.968v-1.032h4v1.032zm-14-8.541v-2.491h24v2.605c0 5.289-24 5.133-24-.114zm9-7.491c-1.104 0-2 .896-2 2v2h2v-1.5c0-.276.224-.5.5-.5h5c.276 0 .5.224.5.5v1.5h2v-2c0-1.104-.896-2-2-2h-6z"/></svg></div></router-link> 
      <router-link to="/contact" class="nav-link"><div class="bg-icon p-2 rounded-circle"><svg xmlns="http://www.w3.org/2000/svg" fill="white" width="24" height="18" viewBox="0 0 24 24"><path d="M.026 24l11.974-11.607 11.974 11.607h-23.948zm11.964-23.961l-11.99 8.725v12.476l7.352-7.127-5.653-4.113 10.291-7.488 10.309 7.488-5.655 4.108 7.356 7.132v-12.476l-12.01-8.725z"/></svg></div></router-link> 
      <router-link to="/blog" class="nav-link"><div class="bg-icon p-2 rounded-circle"><svg xmlns="http://www.w3.org/2000/svg" fill="white" width="24" height="20" viewBox="0 0 24 24"><path d="M19.619 21.671c-5.038 1.227-8.711-1.861-8.711-5.167 0-3.175 3.11-5.467 6.546-5.467 3.457 0 6.546 2.309 6.546 5.467 0 1.12-.403 2.22-1.117 3.073-.029 1 .558 2.435 1.088 3.479-1.419-.257-3.438-.824-4.352-1.385zm-10.711-5.167c0-4.117 3.834-7.467 8.546-7.467.886 0 1.74.119 2.544.338-.021-4.834-4.761-8.319-9.998-8.319-5.281 0-10 3.527-10 8.352 0 1.71.615 3.391 1.705 4.695.047 1.527-.851 3.718-1.661 5.313 2.168-.391 5.252-1.258 6.649-2.115.803.196 1.576.304 2.328.363-.067-.379-.113-.765-.113-1.16z"/></svg></div></router-link> 
      <router-link v-if="getIsAuthenticated" to="/admin/resume" class="nav-link"><div class="bg-icon p-2 rounded-circle"><svg xmlns="http://www.w3.org/2000/svg" fill="white" width="24" height="18" viewBox="0 0 24 24"><path d="M12 0c-6.627 0-12 5.373-12 12s5.373 12 12 12 12-5.373 12-12-5.373-12-12-12zm-.757 2.14c.255-.02.51-.029.757-.029s.502.01.757.029v3.115c-.251-.028-.505-.042-.757-.042s-.506.014-.757.042v-3.115zm-5.765 7.977l-2.879-1.193c.156-.478.351-.948.58-1.399l2.879 1.193c-.245.443-.44.913-.58 1.399zm1.217-2.35l-2.202-2.204c.329-.383.688-.742 1.071-1.071l2.203 2.203c-.396.317-.755.676-1.072 1.072zm.794-4.569c.449-.231.918-.428 1.396-.586l1.205 2.874c-.486.142-.954.339-1.396.586l-1.205-2.874zm4.511 14.31c-1.358 0-2.459-1.101-2.459-2.459 0-.927.513-1.734 1.27-2.153l1.189-5.572 1.189 5.572c.757.419 1.271 1.226 1.271 2.153-.001 1.358-1.102 2.459-2.46 2.459zm1.884-12.029l1.193-2.879c.479.157.948.352 1.399.581l-1.193 2.878c-.444-.246-.913-.44-1.399-.58zm2.349 1.216l2.203-2.203c.383.329.742.688 1.071 1.071l-2.203 2.203c-.316-.395-.675-.754-1.071-1.071zm2.259 3.321c-.147-.483-.35-.95-.603-1.39l2.86-1.238c.235.445.437.912.602 1.39l-2.859 1.238z"/></svg></div></router-link> 
    </div>
      <div v-else class="z-index-100 position-fixed h-100 d-flex flex-column justify-content-center float-right-15px">
        <router-link to="/" class="nav-link my-3"><span class="nav-item rounded-5   d-flex align-items-center justify-content-end"><span class="text-light d-none ps-3  nav-item-text">HOME</span>  <span class="bg-icon rounded-circle p-2"><svg xmlns="http://www.w3.org/2000/svg" fill="white" width="24" height="15" viewBox="0 0 24 24"><path d="M21 13v10h-6v-6h-6v6h-6v-10h-3l12-12 12 12h-3zm-1-5.907v-5.093h-3v2.093l3 3z"/></svg></span></span></router-link> 
        <router-link to="/about" class="nav-link my-3"><span class="nav-item rounded-5 d-flex align-items-center justify-content-end"><span class="text-light ps-3 d-none nav-item-text">ABOUT</span><span class="bg-icon rounded-circle p-2"><svg xmlns="http://www.w3.org/2000/svg" fill="white" width="24" height="15" viewBox="0 0 24 24"><path d="M19 7.001c0 3.865-3.134 7-7 7s-7-3.135-7-7c0-3.867 3.134-7.001 7-7.001s7 3.134 7 7.001zm-1.598 7.18c-1.506 1.137-3.374 1.82-5.402 1.82-2.03 0-3.899-.685-5.407-1.822-4.072 1.793-6.593 7.376-6.593 9.821h24c0-2.423-2.6-8.006-6.598-9.819z"/></svg></span></span></router-link> 
        <router-link to="/portfolio" class="nav-link my-3"><span class="nav-item rounded-5 d-flex align-items-center justify-content-end"><span class="text-light ps-3 d-none nav-item-text">PORTFOLIO</span><span class="bg-icon rounded-circle p-2"><svg xmlns="http://www.w3.org/2000/svg" fill="white" width="24" height="18" viewBox="0 0 24 24"><path d="M12.23 15.5c-6.801 0-10.367-1.221-12.23-2.597v9.097h24v-8.949c-3.218 2.221-9.422 2.449-11.77 2.449zm1.77 2.532c0 1.087-.896 1.968-2 1.968s-2-.881-2-1.968v-1.032h4v1.032zm-14-8.541v-2.491h24v2.605c0 5.289-24 5.133-24-.114zm9-7.491c-1.104 0-2 .896-2 2v2h2v-1.5c0-.276.224-.5.5-.5h5c.276 0 .5.224.5.5v1.5h2v-2c0-1.104-.896-2-2-2h-6z"/></svg></span></span></router-link> 
        <router-link to="/contact" class="nav-link my-3"><span class="nav-item rounded-5 d-flex align-items-center justify-content-end"><span class="text-light ps-3 d-none nav-item-text">CONTACT</span><span class="bg-icon rounded-circle p-2"><svg xmlns="http://www.w3.org/2000/svg" fill="white" width="24" height="18" viewBox="0 0 24 24"><path d="M.026 24l11.974-11.607 11.974 11.607h-23.948zm11.964-23.961l-11.99 8.725v12.476l7.352-7.127-5.653-4.113 10.291-7.488 10.309 7.488-5.655 4.108 7.356 7.132v-12.476l-12.01-8.725z"/></svg></span></span></router-link> 
        <router-link to="/blog" class="nav-link my-3"><span class="nav-item rounded-5 d-flex align-items-center justify-content-end"><span class="text-light ps-3  d-none nav-item-text">BLOG</span><span class="bg-icon rounded-circle p-2"><svg xmlns="http://www.w3.org/2000/svg" fill="white" width="24" height="20" viewBox="0 0 24 24"><path d="M19.619 21.671c-5.038 1.227-8.711-1.861-8.711-5.167 0-3.175 3.11-5.467 6.546-5.467 3.457 0 6.546 2.309 6.546 5.467 0 1.12-.403 2.22-1.117 3.073-.029 1 .558 2.435 1.088 3.479-1.419-.257-3.438-.824-4.352-1.385zm-10.711-5.167c0-4.117 3.834-7.467 8.546-7.467.886 0 1.74.119 2.544.338-.021-4.834-4.761-8.319-9.998-8.319-5.281 0-10 3.527-10 8.352 0 1.71.615 3.391 1.705 4.695.047 1.527-.851 3.718-1.661 5.313 2.168-.391 5.252-1.258 6.649-2.115.803.196 1.576.304 2.328.363-.067-.379-.113-.765-.113-1.16z"/></svg></span></span></router-link> 
        <router-link v-if="getIsAuthenticated" to="/admin/resume" class="nav-link my-3"><span class="nav-item rounded-5 d-flex align-items-center justify-content-end"><span class="text-light ps-3  d-none nav-item-text">Dasboard</span><span class="bg-icon rounded-circle p-2"><svg xmlns="http://www.w3.org/2000/svg" fill="white" width="24" height="20" viewBox="0 0 24 24"><path d="M12 0c-6.627 0-12 5.373-12 12s5.373 12 12 12 12-5.373 12-12-5.373-12-12-12zm-.757 2.14c.255-.02.51-.029.757-.029s.502.01.757.029v3.115c-.251-.028-.505-.042-.757-.042s-.506.014-.757.042v-3.115zm-5.765 7.977l-2.879-1.193c.156-.478.351-.948.58-1.399l2.879 1.193c-.245.443-.44.913-.58 1.399zm1.217-2.35l-2.202-2.204c.329-.383.688-.742 1.071-1.071l2.203 2.203c-.396.317-.755.676-1.072 1.072zm.794-4.569c.449-.231.918-.428 1.396-.586l1.205 2.874c-.486.142-.954.339-1.396.586l-1.205-2.874zm4.511 14.31c-1.358 0-2.459-1.101-2.459-2.459 0-.927.513-1.734 1.27-2.153l1.189-5.572 1.189 5.572c.757.419 1.271 1.226 1.271 2.153-.001 1.358-1.102 2.459-2.46 2.459zm1.884-12.029l1.193-2.879c.479.157.948.352 1.399.581l-1.193 2.878c-.444-.246-.913-.44-1.399-.58zm2.349 1.216l2.203-2.203c.383.329.742.688 1.071 1.071l-2.203 2.203c-.316-.395-.675-.754-1.071-1.071zm2.259 3.321c-.147-.483-.35-.95-.603-1.39l2.86-1.238c.235.445.437.912.602 1.39l-2.859 1.238z"/></svg></span></span></router-link> 
      </div>
     <router-view/>
  </nav>
 
</template>

<style>
*{
  box-sizing: border-box;
}
 .nav-item:hover .nav-item-text{
  display: inline-block !important;
}
.nav-item:hover{
  background-color: var(--my-red);
}
.nav-item:hover .bg-icon{
  background-color: var(--my-red);

}
.nav-item{
  transition: .3s;
}
nav a.router-link-exact-active .bg-icon{
  background-color: var(--my-red);
}

.bg-gray{
  background-color: #2b2a2a;
}
.bg-icon{
  background-color: #444444;
  transition: .3s;
}
.bg-icon:hover{
  background-color: var(--my-red);
}
.float-right-15px{
  right: 30px;
}
.my-p-10{
  padding:10px;
}
.z-index-100{
  z-index: 100;
}
@media screen and (max-width: 991px) {
  .bg-gray{
  background-color: #2b2a2a;}
  
}
@media screen and (min-width: 992px) and (max-width: 1200px) {
  
  }
</style>
<script>
export default {
  data(){
    return{
      window: {
            width: 0,
            height: 0
        }
    }},
    
    computed:{
      
        getIsAuthenticated(){
          return this.$store.getters.getIsAuthenticated
        }
      
    },
    created() {
        window.addEventListener('resize', this.handleResize);
        this.handleResize();
        this.$store.dispatch("fetchBlogs"),
        this.$store.dispatch("fetchTags")
        this.$store.dispatch("fetchPortfolios")
        this.$store.dispatch('fetchAbout')
      this.$store.dispatch("fetchSkills")
    },
    unmounted() {
        window.removeEventListener('resize', this.handleResize);
    },
    methods: {
        handleResize() {
            this.window.width = window.innerWidth;
            this.window.height = window.innerHeight;
        }
    },
    
  }
</script>