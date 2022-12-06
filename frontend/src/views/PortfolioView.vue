<template>
  <div class="portfolio mb-5 pb-5">
    <!-- MY PORTFOLIO -->
    <div class="text-sm-center w-100">
      <h3 class="position-absolute z-index-1 w-100 ps-3 mt-5"><span class="text-light">MY</span> <span class="text-red">PORTFOLIO</span></h3>
      <h1 class="position-relative z-index-2 w-100 mt-5">WORKS</h1>
    </div>
    
    <!-- Personal Info -->
    <div class="container-xl my-5 py-5 my-sm-0 text-light">
      <div v-if="portfolio_len>1" class="d-flex justify-content-md-center flex-wrap">
        <div @click="change_all()" class="me-4 category text-yellow-hover" :class="{'text-yellow':selected_category=='all'}">ALL</div>
        <div @click="change_category(category)" class="me-4 category text-yellow-hover" :class="{'text-yellow':selected_category==category}" v-for="category in categories" :key="category">{{category.category}}</div>
      </div>
      <div class="row mt-5" >
        <div @click="select_modal(project)" :key="project" v-for="project in selected_projects" class="col col-12 col-sm-6 col-lg-4 mb-4" data-bs-toggle="modal" data-bs-target="#modalId">
          <div class="project rounded">
            <video class="w-100 h-100" v-if="project.video">
              <source :src="project.video">
            </video>
            <img v-else class="w-100 h-100" :src="project.image" alt="">
            <div class="w-100 h-100 d-flex justify-content-center align-items-center"><strong>{{project.title}}</strong></div>
          </div>
        </div>   
      </div>

    </div>
     <div v-if="modal" class="modal fade" id="modalId" tabindex="-1" data-bs-backdrop="static" data-bs-keyboard="false" role="dialog" aria-labelledby="modalTitleId" aria-hidden="true">
      <div class="d-flex justify-content-center flex-column modal-dialog modal-dialog-scrollable modal-dialog-centered modal-md modal-project" role="document">
        <div class="modal-content bg-transparent text-light px-3 py-1 px-sm-0">
          <div class="d-flex justify-content-end">
              <span class="cursor-pointer" data-bs-dismiss="modal" aria-label="Close"><svg fill="white" xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24"><path d="M12 2c5.514 0 10 4.486 10 10s-4.486 10-10 10-10-4.486-10-10 4.486-10 10-10zm0-2c-6.627 0-12 5.373-12 12s5.373 12 12 12 12-5.373 12-12-5.373-12-12-12zm6 16.094l-4.157-4.104 4.1-4.141-1.849-1.849-4.105 4.159-4.156-4.102-1.833 1.834 4.161 4.12-4.104 4.157 1.834 1.832 4.118-4.159 4.143 4.102 1.848-1.849z"/></svg></span>
            </div>
        </div>
        <div class="modal-content bg-gray text-light p-3 rounded-4 p-4">
          <h2 class="text-center text-yellow my-2">{{modal.title}}</h2>
          <div class="row">
            <div class="col col-12 col-sm-6 my-1"><span class="me-2"><svg xmlns="http://www.w3.org/2000/svg" fill="white" width="14" height="14" viewBox="0 0 24 24"><path d="M11.362 2c4.156 0 2.638 6 2.638 6s6-1.65 6 2.457v11.543h-16v-20h7.362zm.827-2h-10.189v24h20v-14.386c0-2.391-6.648-9.614-9.811-9.614zm4.811 13h-10v-1h10v1zm0 2h-10v1h10v-1zm0 3h-10v1h10v-1z"/></svg></span><small>Project: </small><small>{{modal.project}}</small></div>
            <div class="col col-12 col-sm-6 my-1"><span class="me-2"><svg xmlns="http://www.w3.org/2000/svg" fill="white" width="14" height="14" viewBox="0 0 24 24"><path d="M12 2c2.757 0 5 2.243 5 5.001 0 2.756-2.243 5-5 5s-5-2.244-5-5c0-2.758 2.243-5.001 5-5.001zm0-2c-3.866 0-7 3.134-7 7.001 0 3.865 3.134 7 7 7s7-3.135 7-7c0-3.867-3.134-7.001-7-7.001zm6.369 13.353c-.497.498-1.057.931-1.658 1.302 2.872 1.874 4.378 5.083 4.972 7.346h-19.387c.572-2.29 2.058-5.503 4.973-7.358-.603-.374-1.162-.811-1.658-1.312-4.258 3.072-5.611 8.506-5.611 10.669h24c0-2.142-1.44-7.557-5.631-10.647z"/></svg></span><small>Client: </small><small>{{modal.client}}</small></div>
            <div class="col col-12 col-sm-6 my-1"><span class="me-2"><svg xmlns="http://www.w3.org/2000/svg" fill="white" width="14" height="14" viewBox="0 0 24 24"><path d="M24 10.935v2.131l-8 3.947v-2.23l5.64-2.783-5.64-2.79v-2.223l8 3.948zm-16 3.848l-5.64-2.783 5.64-2.79v-2.223l-8 3.948v2.131l8 3.947v-2.23zm7.047-10.783h-2.078l-4.011 16h2.073l4.016-16z"/></svg></span><small>Language: </small><small v-for="lang in modal.languages" :key="lang"><span v-if="modal.languages[modal.languages.length-1]!=lang">{{lang.name}}, </span><span v-else>{{lang.name}}</span></small></div>
            <div class="col col-12 col-sm-6 my-1"><span class="me-2"><svg xmlns="http://www.w3.org/2000/svg" fill="white" width="14" height="14" viewBox="0 0 24 24"><path d="M6 17c2.269-9.881 11-11.667 11-11.667v-3.333l7 6.637-7 6.696v-3.333s-6.17-.171-11 5zm12 .145v2.855h-16v-12h6.598c.768-.787 1.561-1.449 2.339-2h-10.937v16h20v-6.769l-2 1.914z"/></svg></span><small>Preview: </small><a :href="'http://'+modal.preview" class="text-yellow">{{modal.preview}}</a></div>
            <video class="my-3" v-if="modal.video" controls>
              <source :src="modal.video">
            </video>
            <img v-else class="modal_image my-3" :src="modal.image" alt="">
          </div>
        </div>
      </div>
    </div> 
 </div>

</template>
<script>
import axios from 'axios';
import { mapGetters } from 'vuex';
export default {
  name:"PortfolioView",
  
  methods:{
    select_modal(modal){
      this.modal=modal
      console.log(modal)
    },
    change_category(element){
      this.selected_projects=this.projects.filter(project=>project.category==element.category)
      console.log(this.selected_projects)
      console.log(element)
      this.selected_category=element
    },
    change_all(){
      this.selected_category="all"
      this.selected_projects=this.projects
    }
  },
  data(){
    return{
      selected_projects:null,
      selected_category:"all",
      categories:null,
      projects:null,
      modal:null
  }
} 
,created(){
        axios.get("http://localhost:8000/portfolios/").then(data=>console.log(this.selected_projects=data.data));
        axios.get("http://localhost:8000/portfolios/").then(data=>console.log(this.projects=data.data));
        axios.get("http://localhost:8000/portfolios/categories/").then(data=>console.log(this.categories=data.data))
},
computed:{
  ...mapGetters({
    portfolio_len:"getPortfolioLen"
  })
}

}
</script>
<style>

  .modal_image{
    border-radius: 15px !important;
    overflow: hidden;
  }
  .project{
    cursor: pointer;
    position: relative;
    overflow: hidden;
    width: 100%;
    height: 229px;
    background-size: cover;
    background-position: center;
  }
  .project div{
    transition: .3s;
    top:-50px;
    position: absolute;
    opacity: 0;
  }
  .project:hover div{
    background-color: var(--my-yellow);
    height: 100%;
    top: 0;
    opacity: 1;
  }
  .category{
    cursor: pointer;
  }
</style>