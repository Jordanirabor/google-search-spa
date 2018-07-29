    // src/components/Insert.vue
	
    <template>
    <div>
    <section>
      
    <div class="container">
    <form>
    <input type="name" ref="name" placeholder="Name" required>
    <textarea ref="body" placeholder="Body" required></textarea>
    <button name="send" type="submit" v-on:click.prevent="insertData" class="submit">SEND</button>
      
    </form>
     
    </div>
    </section>
    </div>
    </template>
    
    <script>
    
    export default {
      name: 'insert',
      methods: {
        insertData: function(){
          let name = this.$refs.name.value
          let  body = this.$refs.body.value
          fetch('/api/insert', {
            method: 'POST',
            headers: {
              'Accept': 'application/json',
              'Content-Type': 'application/json'
        },
        body: JSON.stringify({name: name, body: body})
      });
      this.$refs.name.value = ""
      this.$refs.body.value = ""
        }
      }
    }
    
    </script>
    
    <style scoped>
    
    form {
      margin: 6em 0em;
    }
    
    section .container form input,
    section .container form textarea {
      width:97.4%;
      height:30px;
      padding:5px 10px;
      font-size: 12px;
      color:#999;
      letter-spacing:1px;
      background: #FFF;
      border:2px solid #FFF;
      margin-bottom:25px;
      -webkit-transition:all .1s ease-in-out;
      -moz-transition:all .1s ease-in-out;
      -ms-transition:all .1s ease-in-out;
      -o-transition:all .1s ease-in-out;
      transition:all .1s ease-in-out;
      }
      
    section .container form input:focus,
    section .container form textarea:focus {
      border:2px solid #00b0ff;
      color:#999;
      }
      
    section .container form textarea {
      height:150px;
      }
      
    section .container form .submit {
      width:100%;
      padding:5px 10px;
      font-size: 12px;
      letter-spacing:1px;
      background:#0091ea;
      height:40px;
      text-transform:uppercase;
      letter-spacing:1px;
      color:#FFF;
      -webkit-transition:all .1s ease-in-out;
      -moz-transition:all .1s ease-in-out;
      -ms-transition:all .1s ease-in-out;
      -o-transition:all .1s ease-in-out;
      transition:all .1s ease-in-out;
      }
      
    section .container form .submit:hover {
      color:#FFF;
      background: #00b0ff;
      cursor:pointer;
      }
      
    section .container form .required {
      color:#b43838;
      }
      
    </style>