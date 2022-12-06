<template>
  <div class="portfolio mb-5 pb-5">
    <!-- MY PORTFOLIO -->
    <div class="text-sm-center w-100">
      <h3 class="position-absolute z-index-1 w-100 ps-3 mt-5"><span class="text-light">MY</span> <span class="text-yellow">BLOG</span></h3>
      <h1 class="position-relative z-index-2 w-100 mt-5">POSTS</h1>
    </div>
    
    <!-- Personal Info -->
    <div class="container-xl my-5 py-5 my-sm-0 text-light">
      <div class="row" >
        <div @click="select_blog(blog)" :key="blog" v-for="blog in blogs" class="col col-12 col-md-6 col-xl-4 mb-4 cursor-pointer" data-bs-toggle="modal" data-bs-target="#modalId">
            <div class="card overflow-hidden bg-gray blog">
              <div class="blog_image">
                <video class="w-100" v-if="blog.video">
                  <source :src="blog.video">
                </video>
                <img v-else class="h-100 w-100" :src="blog.image" alt="Title">
              </div>
              <div class="card-body">
                <h4 class="card-title">{{blog.title}}</h4>
                <p class="card-text">{{blog.description_part1.slice(0,70)}} . . .</p>
              </div>
            </div>
        </div>
        
      </div>
      
    </div>
 
  
  <!-- Modal Body -->
  <!-- if you want to close by clicking outside the modal, delete the last endpoint:data-bs-backdrop and data-bs-keyboard -->
  <div v-if="modal" class="modal fade" id="modalId" tabindex="-1" data-bs-backdrop="static" data-bs-keyboard="false" role="dialog" aria-labelledby="modalTitleId" aria-hidden="true">
    <div class="modal-dialog modal-dialog-scrollable modal-dialog-centered modal-md" role="document">
      <div class="modal-content bg-transparent border-0 blog-modal">
        <div class="d-flex justify-content-end modal-close">
              <span class="cursor-pointer" data-bs-dismiss="modal" aria-label="Close"><svg fill="white" xmlns="http://www.w3.org/2000/svg" width="45" height="45" viewBox="0 0 24 24"><path d="M12 2c5.514 0 10 4.486 10 10s-4.486 10-10 10-10-4.486-10-10 4.486-10 10-10zm0-2c-6.627 0-12 5.373-12 12s5.373 12 12 12 12-5.373 12-12-5.373-12-12-12zm6 16.094l-4.157-4.104 4.1-4.141-1.849-1.849-4.105 4.159-4.156-4.102-1.833 1.834 4.161 4.12-4.104 4.157 1.834 1.832 4.118-4.159 4.143 4.102 1.848-1.849z"/></svg></span>
        </div>
        <div class="modal-body bg-gray rounded my-2 p-md-5 pt-md-0 text-light">
          <h1 class="my-5"><span class="text-light">POST </span><span class="text-yellow">DETAILS</span></h1>
          <div class="d-flex flex-wrap">
            <div class="me-4">
              <span class="me-1"><svg xmlns="http://www.w3.org/2000/svg" fill="orange" width="12" height="12" viewBox="0 0 24 24"><path d="M19 7.001c0 3.865-3.134 7-7 7s-7-3.135-7-7c0-3.867 3.134-7.001 7-7.001s7 3.134 7 7.001zm-1.598 7.18c-1.506 1.137-3.374 1.82-5.402 1.82-2.03 0-3.899-.685-5.407-1.822-4.072 1.793-6.593 7.376-6.593 9.821h24c0-2.423-2.6-8.006-6.598-9.819z"/></svg></span>
              <span><small>{{modal.region}}</small></span>
            </div>
            <div class="me-4">
              <span class="me-1"><svg xmlns="http://www.w3.org/2000/svg" fill="orange" width="12" height="12" viewBox="0 0 24 24"><path d="M20 20h-4v-4h4v4zm-6-10h-4v4h4v-4zm6 0h-4v4h4v-4zm-12 6h-4v4h4v-4zm6 0h-4v4h4v-4zm-6-6h-4v4h4v-4zm16-8v22h-24v-22h3v1c0 1.103.897 2 2 2s2-.897 2-2v-1h10v1c0 1.103.897 2 2 2s2-.897 2-2v-1h3zm-2 6h-20v14h20v-14zm-2-7c0-.552-.447-1-1-1s-1 .448-1 1v2c0 .552.447 1 1 1s1-.448 1-1v-2zm-14 2c0 .552-.447 1-1 1s-1-.448-1-1v-2c0-.552.447-1 1-1s1 .448 1 1v2z"/></svg></span>
              <span><small>{{format_date(modal.date)}}</small></span>
            </div>
            <div class="me-4">
              <span class="me-1"><svg xmlns="http://www.w3.org/2000/svg" fill="orange" width="12" height="12" viewBox="0 0 24 24"><path d="M12.878 2h-8.877l-.001 9.014 10.973 11.123 9.026-9.027-11.121-11.11zm-5.615 3.263c.684-.684 1.791-.684 2.475 0 .684.683.684 1.791 0 2.474s-1.791.684-2.475 0-.684-1.791 0-2.474zm7.719 14.036l-6.225-6.349 6.121-6.122 6.293 6.283-6.189 6.188zm-3.379 2.265l-1.369 1.436-10.234-10.257.001-7.743h1.999v6.891l9.603 9.673z"/></svg></span>
              <span><small class="text-lowercase" v-for="tag in modal.tags" :key="tag"><span>{{tag.name}}</span><span v-if="modal.tags[modal.tags.length-1]!=tag">, </span></small></span>
            </div>
          </div>
          <h4 class="mt-2">{{modal.title}}</h4>
          <video v-if="modal.video" class="modal_image my-3 w-100" controls>
            <source :src="modal.video">
          </video>
          <iframe v-else-if="modal.iframe_src" class="modal_image my-3 w-100" height="500" :src="modal.iframe_src" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
          <img v-else class="modal_image my-3 w-100" :src="modal.image" alt="">
          <div class="my-1">{{modal.description_part1}}</div>
          <div v-if="modal.remember" class="d-flex my-4"><span class="me-3"><svg xmlns="http://www.w3.org/2000/svg" fill="white" width="50" height="50" viewBox="0 0 24 24"><path d="M14.017 21v-7.391c0-5.704 3.731-9.57 8.983-10.609l.995 2.151c-2.432.917-3.995 3.638-3.995 5.849h4v10h-9.983zm-14.017 0v-7.391c0-5.704 3.748-9.57 9-10.609l.996 2.151c-2.433.917-3.996 3.638-3.996 5.849h3.983v10h-9.983z"/></svg></span><span><i>{{modal.remember}}</i></span></div>
          <div v-if="modal.description_part2">{{modal.description_part2}}</div>
        </div>
      </div>
    </div>
  </div>
</div>
</template>
<script>
import axios from 'axios';
import moment from 'moment'
export default {
  name:"PortfolioView",
  methods:{
      format_date(value){
         if (value) {
           return moment(String(value)).format('DD MMMM YYYY')
          }
      },
    select_blog(e){
      this.modal=e
      console.log(e)
    },
  },
  data(){
    return{
      blogs:null,
      modal:null
  }
} 
,created(){
        axios.get("http://localhost:8000/blogs/").then(data=>console.log(this.blogs=data.data));
    }
}
</script>
<style>
.modal{
  --bs-modal-width:800px;
}
.blog-modal h1{
  font-size: 50px !important;
  font-weight: bold;
}
.blog-modal h4{
  font-size: 35px !important;
  font-weight: bold;
}
.blog_image{
  display: flex;
  justify-content: center;
  align-items: center;
  overflow: hidden;
  border-bottom: 6px solid var(--my-yellow);
}
 
  .blog:hover h4{
    color: var(--my-yellow) !important;
  }
  .modal_image{
    border-radius: 10px !important;
    overflow: hidden;
  }

</style>