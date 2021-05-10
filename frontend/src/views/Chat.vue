<template>
  <div id="chatList">

  </div>
  <div id="addMessage">

  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Chat",
  data(){
    return{
      comments: [],
      loadedComments: false,
      noComments: true,
    }
  },
  mounted(){
    this.getComments();
  },
  methods: {
    getComments(){
       axios
            .get("api/chat").then((response) => {
              this.loadedComments = false;
              for (let i = 0; i < response.data.data.length; i++) {
                this.comments.push(response.data.data[i]);
              }
              if (response.data.data.length === 0) {
                this.noComments = true;
              }
              this.loadedComments = true;
            })
            .catch((error) => {
              console.error(error);
              this.loadedComments = false;
            });
    }
  }
}
</script>

<style scoped>
#chatList {
  width: 80vw;
  height: 70vh;
  margin: auto;
  background: lightgrey;
  box-shadow: 0 0 20px #19191B;
}
#addMessage {
  width: 80vw;
  height: 30px;
  margin: auto;
  background: #464649;
}
</style>