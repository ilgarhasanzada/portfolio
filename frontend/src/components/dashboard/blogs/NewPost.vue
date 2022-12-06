<template>
  <div class="col col-12 col-md-5 bg-dark rounded p-2">
    <form enctype="multipart/form-data">
        <h2>New Post</h2>
        <img class="w-100 rounded mb-3" :src="image" alt="">

        <div class="mb-3">
          <label for="title" class="form-label">Title</label>
          <input type="text"
            class="form-control bg-dark border-secondary text-light" v-model="data.title" id="title" aria-describedby="helpId" placeholder="Title">
        </div>
        <div class="mb-3">
          <label for="part_1" class="form-label">Description part 1</label>
          <textarea class="form-control bg-dark border-secondary text-light" v-model="data.description_part1" placeholder="Description part 1" name="" id="part_1" rows="3"></textarea>
        </div>
        <div class="mb-3">
          <label for="remember" class="form-label">Remember</label>
          <textarea class="form-control bg-dark border-secondary text-light" v-model="data.remember" placeholder="Remember" name="" id="remember" rows="3"></textarea>
        </div>
        <div class="mb-3">
          <label for="part_2" class="form-label">Description part 2</label>
          <textarea class="form-control bg-dark border-secondary text-light" v-model="data.description_part2" placeholder="Description part 2" id="part_2" rows="3"></textarea>
        </div>
       <div class="mb-3 d-flex">
         <label for="image" class="form-label  cursor-pointer bg-secondary p-2 btn text-dark">
          <svg xmlns="http://www.w3.org/2000/svg" fill="black" width="24" height="24" viewBox="0 0 24 24"><path d="M5 4h-3v-1h3v1zm8 6c-1.654 0-3 1.346-3 3s1.346 3 3 3 3-1.346 3-3-1.346-3-3-3zm11-5v17h-24v-17h5.93c.669 0 1.293-.334 1.664-.891l1.406-2.109h8l1.406 2.109c.371.557.995.891 1.664.891h3.93zm-19 4c0-.552-.447-1-1-1s-1 .448-1 1 .447 1 1 1 1-.448 1-1zm13 4c0-2.761-2.239-5-5-5s-5 2.239-5 5 2.239 5 5 5 5-2.239 5-5z"/></svg>
          Upload Photo
        </label>
         <input ref="file" accept="image/" @change="preview_image" type="file" class="form-control d-none" name="" id="image" placeholder="">
         <label for="video" class="mx-2 form-label cursor-pointer bg-secondary p-2 btn text-dark">
          <svg fill="black" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><path d="M11.266 7l12.734-2.625-.008-.042-1.008-4.333-21.169 4.196c-1.054.209-1.815 1.134-1.815 2.207v14.597c0 1.657 1.343 3 3 3h18c1.657 0 3-1.343 3-3v-14h-12.734zm8.844-5.243l2.396 1.604-2.994.595-2.398-1.605 2.996-.594zm-5.898 1.169l2.4 1.606-2.994.595-2.401-1.607 2.995-.594zm-5.904 1.171l2.403 1.608-2.993.595-2.406-1.61 2.996-.593zm-2.555 5.903l2.039-2h3.054l-2.039 2h-3.054zm4.247 10v-7l6 3.414-6 3.586zm4.827-10h-3.054l2.039-2h3.054l-2.039 2zm6.012 0h-3.054l2.039-2h3.054l-2.039 2z"/></svg>
          Upload Video
        </label>
         <input @change="preview_video" type="file" class="form-control d-none" name="" id="video" placeholder="">
        </div>
        <div class="mb-3">
          <label for="youtube" class="form-label">Youtube link</label>
          <textarea class="form-control bg-dark border-secondary text-light" v-model="data.iframe_src" placeholder="Youtube link" name="" id="youtube" rows="3"></textarea>
        </div>
        <div class="mb-3">
         <label for="tags" class="form-label">Tags</label>
         <select multiple class="form-select form-select-md bg-dark border-secondary text-light" name="" id="tags">
          <option class="text-capitalize" v-for="tag in tags" :key="tag">{{tag.name}}</option>
        </select>
       </div>
       <div class="mb-3">
         <label for="province" class="form-label">Province</label>
         <input type="text"
           class="form-control bg-dark border-secondary text-light" name="" id="province" v-model="data.region" aria-describedby="helpId" placeholder="Province">
       </div>
       <div class="float-right d-flex justify-content-end">
        <button @click="create()" type="button" class="btn btn-secondary p-2 my-3">Create</button>
       </div>
    </form>
    </div>
</template>

<script>
import axios from 'axios';
export default {
    name:"NewPost",
    props:{
        tags:Object
    },
    data(){
        return{
            data:{
                "title": "",
                "description_part1": "",
                "remember": "",
                "description_part2": "",
                "image": "",
                "video": "",
                "iframe_src": "",
                "region": ""
            },
            "image":null
        }
    },
    methods:{
        async create(){
            let formData = new FormData();
            formData.append('title',this.data.title)
            formData.append('description_part1',this.data.description_part1)
            formData.append('remember',this.data.remember)
            formData.append('description_part2',this.data.description_part2)
            formData.append('image',this.data.image)
            formData.append('video',this.data.video)
            formData.append('iframe_src',this.data.iframe_src)
            formData.append('region',this.data.region)
            const config = {
              header: { "content_type": "multipart/form-data" }
            }
            await axios.post("blogs/",formData,config).then(response=>{
              console.log(response)
            })
            .catch(error=>{
              console.log(error.response.data)
            })  
              this.$store.dispatch('actionAddBlog',this.data)
              this.$router.push('/admin/blogs')
        },
        preview_image(event){
            this.data.image =event.target.files[0]
            this.image =event.target.files[0]
            const reader = new FileReader()
            reader.readAsDataURL(this.image)
            reader.onload=e=>{
                this.image=e.target.result            
            }},
          preview_video(event){
            this.data.video=event.target.files[0]
        }
      
        
      }
    }
  

</script>

<style>

</style>