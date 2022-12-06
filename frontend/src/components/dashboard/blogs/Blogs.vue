<template>
    <div class="row justify-content-center p-2 mb-5">
       <div class="col col-12  m-2 rounded">
        <div class="table-responsive">
          <table class="table table-dark">
            <thead>
              <tr>
                <th class="align-middle" scope="col" >
                  <input @click="select_all()" type="checkbox" class="me-2" name="" id="select-all"> 
                </th>
                <th class="align-middle" scope="col">Title</th>
                <th class="align-middle" scope="col">Date</th>
                <th class="align-middle" scope="col">
                  <span v-if="deleted_posts.length==0"><svg fill="gray" xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24"><path d="M3 6v18h18v-18h-18zm5 14c0 .552-.448 1-1 1s-1-.448-1-1v-10c0-.552.448-1 1-1s1 .448 1 1v10zm5 0c0 .552-.448 1-1 1s-1-.448-1-1v-10c0-.552.448-1 1-1s1 .448 1 1v10zm5 0c0 .552-.448 1-1 1s-1-.448-1-1v-10c0-.552.448-1 1-1s1 .448 1 1v10zm4-18v2h-20v-2h5.711c.9 0 1.631-1.099 1.631-2h5.315c0 .901.73 2 1.631 2h5.712z"/></svg></span>
                  <span v-else data-bs-toggle="modal" data-bs-target="#deleteBlogs"><svg class="cursor-pointer" fill="red" xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24"><path d="M3 6v18h18v-18h-18zm5 14c0 .552-.448 1-1 1s-1-.448-1-1v-10c0-.552.448-1 1-1s1 .448 1 1v10zm5 0c0 .552-.448 1-1 1s-1-.448-1-1v-10c0-.552.448-1 1-1s1 .448 1 1v10zm5 0c0 .552-.448 1-1 1s-1-.448-1-1v-10c0-.552.448-1 1-1s1 .448 1 1v10zm4-18v2h-20v-2h5.711c.9 0 1.631-1.099 1.631-2h5.315c0 .901.73 2 1.631 2h5.712z"/></svg></span>
                </th>
                <th class="align-middle text-center" scope="col"><button @click="post_create" class="btn btn-secondary">New Post</button></th>
              </tr>
            </thead>
            <tbody class="text-secondary">
              <tr class="" v-for="blog in blogs" :key="blog">
                <td scope="row" class="align-middle">
                    <input @click="select_deleted_posts(blog)" type="checkbox" class="me-2 checked-blog" name="" > 
                </td>
                <td class="align-middle">{{blog.title}}</td>
                <td class="align-middle">{{format_date(blog.date)}}</td>
                <td class="align-middle">
                  <span data-bs-toggle="modal" data-bs-target="#deleteBlog"  @click="select_deleted_post(blog)"><svg class="cursor-pointer" fill="white" xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24"><path d="M3 6v18h18v-18h-18zm5 14c0 .552-.448 1-1 1s-1-.448-1-1v-10c0-.552.448-1 1-1s1 .448 1 1v10zm5 0c0 .552-.448 1-1 1s-1-.448-1-1v-10c0-.552.448-1 1-1s1 .448 1 1v10zm5 0c0 .552-.448 1-1 1s-1-.448-1-1v-10c0-.552.448-1 1-1s1 .448 1 1v10zm4-18v2h-20v-2h5.711c.9 0 1.631-1.099 1.631-2h5.315c0 .901.73 2 1.631 2h5.712z"/></svg></span>
                </td>
                <td class="align-middle text-center"><button @click="show_detail(blog)" class="btn btn-danger">Detail</button></td>
              </tr>
            </tbody>
          </table>
        </div>
        
      </div>
      <!-- <update-blog v-if="!this.$store.state.new_post"/>
      <new-post v-else :tags="tags"/>
     -->
    <div v-if="deleted_post" class="modal fade" id="deleteBlog" tabindex="-1" data-bs-backdrop="static" data-bs-keyboard="false" role="dialog" aria-labelledby="modalTitleId" aria-hidden="true">
        <div class="modal-dialog modal-dialog-scrollable text-light modal-dialog-centered modal-lg" role="document">
          <div class="modal-content bg-secondary">
            <div class="modal-header">
              <h5 class="modal-title" id="modalTitleId">{{deleted_post.title}}</h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body border-0">
              Do you want to delete this post?
            </div>
            <div class="modal-footer border-0">
              <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
              <button @click="delete_post" type="button" data-bs-dismiss="modal" class="btn btn-primary">Save</button>
            </div>
          </div>
        </div>
    </div>
    <div v-if="deleted_posts" class="modal fade" id="deleteBlogs" tabindex="-1" data-bs-backdrop="static" data-bs-keyboard="false" role="dialog" aria-labelledby="modalTitleId" aria-hidden="true">
        <div class="modal-dialog modal-dialog-scrollable text-light modal-dialog-centered modal-lg" role="document">
          <div class="modal-content bg-secondary">
            <div class="modal-header">
              <h5 class="modal-title" id="modalTitleId"><span v-for="i in deleted_posts" :key="i"><span v-if="i==deleted_posts[deleted_posts.length-1]">{{i.title}}</span><span v-else>{{i.title}}, </span></span></h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body border-0">
              Do you want to delete this post?
            </div>
            <div class="modal-footer border-0">
              <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
              <button @click="delete_selected_posts" type="button" data-bs-dismiss="modal" class="btn btn-primary">Save</button>
            </div>
          </div>
        </div>
    </div>
  </div>
</template>

<script>
import moment from 'moment'
// import UpdateBlog from './UpdateBlog.vue'
// import NewPost from './NewPost.vue'
import { mapGetters } from 'vuex'
export default {
  // components: { UpdateBlog, NewPost },
    name:"BlogsView",
    data(){
    return{
      selected_image:null,
      deleted_post:[],
      deleted_posts:[]
    }
  },
  methods:{
    select_deleted_posts(blog){
      if (this.deleted_posts.includes(blog)){
        this.deleted_posts.splice(this.deleted_posts.indexOf(blog),1)
      }else{
        this.deleted_posts.push(blog)
      }
      if (this.deleted_posts.length==this.blogs.length){
        document.getElementById('select-all').checked=true
      }else{
        document.getElementById('select-all').checked=false

      }
      console.log(this.deleted_posts)
    },
    delete_post(){
      this.$store.dispatch('actionDeleteBlog',this.deleted_post)
    },
    select_deleted_post(post){
      this.deleted_post=post
      
    },
    delete_selected_posts(){
      this.$store.dispatch('actionDeleteAllBlogs',this.deleted_posts)
      this.deleted_posts=[]
    },
    post_create(){
      this.$store.commit("setNewDataTrue")
      this.$router.push('/admin/blog')
    },
    preview_image(event){
      this.selected_image=event.target.files[0].name
    },
    preview_video(event){
      this.selected_video=event.target.files[0].name
    },
    show_detail(data){
      this.$store.commit('setSelectedPost',data)
      this.$store.commit("setNewData")
      this.$router.push('blogs/'+data.id)
    },
    format_date(value){
         if (value) {
           return moment(String(value)).format('DD/MM/YYYY')
          }
      },
    select_all(){
      if (!document.getElementById('select-all').checked){
        this.deleted_posts=[]
        for (const i of document.getElementsByClassName("checked-blog")) {
            i.checked=false
        }
      }else{
        for (const i of document.getElementsByClassName("checked-blog")) {
            i.checked=true
        }
        for (const i of this.blogs) {
          this.deleted_posts.push(i)
        }
      }
      console.log(this.deleted_posts)
    }
  },
  computed:{
    ...mapGetters({
        blogs:'getBlogs',
        tags:'getTags'
      })
  },
 

}
</script>

<style>

</style>