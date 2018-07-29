// src/components/Searchbox.vue
	
    <template>
    <div>
    <nav class="navbar navbar-default navbar-fixed-top navbar-transparent">
         
          <div class="container-fluid">
              <ul class="nav navbar-nav navbar-right nav-large-font">
                <li><a href="#">Gmail</a></li>
                <li><a href="#">Images</a></li>
                <li><a href="#"><span class="glyphicon glyphicon-th"></span></a></li>
                <li><a href="#"><button class="btn btn-sign-in">Sign in</button></a></li>
              </ul>
          </div>
          
        </nav>
        
        <div class="container">
          <div class="container-center">
            <div class="row">
              <div class="text-center col-md-12">
               
                <img src="https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png" alt="Google Logo" id="google-logo">
                
                <div class="form-adjustment">
                  <form action="#" class="form-inline">
                    <div class="form-group">
                      <div class="input-group">
                        <input type="text" class="form-control input-lg" ref="searchbox" list="huge_list" v-on:keyup="hinter" id="gg-search">
                        <div class="input-group-addon input-group-addon-transparent"><i class="fa fa-microphone fa-lg"></i></div>
                      </div>  
                       <datalist id="huge_list" ref="huge_list"></datalist>
                    </div>
                  </form>
                </div>
                 
              </div>
              
              <div class="list-results-container container vertical-center row">
              <div class="list-results col-md-12 text-center"  v-for="(response, index) in responseData">
              <h4 style="color: #609;"> {{ response.name }}  </h4>
              <p style="color: #545454;"> {{ response.body }}  </p>
              <hr/>
              </div>
              </div>
      
            </div>
          </div>
        </div>
        
        <footer class="navbar navbar-default navbar-fixed-bottom">
         
          <div class="container-fluid">
             
              <ul class="nav navbar-nav">    
                <li><a href="#">Advestising</a></li>
                <li><a href="#">Business</a></li>
                <li><a href="#">About</a></li>
              </ul>
              <ul class="nav navbar-nav navbar-right">
                <li><a href="#">Privacy</a></li>
                <li><a href="#">Terms</a></li>
                <li><a href="#">Settings</a></li>
                <li><a href="#">Thank you :)</a></li>
              </ul>
            
          </div>
          
        </footer>
        </div>
    </template>
    
    <script>
    
// src/components/Searchbox.vue
	
    export default {
    
      name: 'Searchbox',
      data () {
        return {
            responseData: []
        }
      },
      
      mounted() {
        // create one global XHR object 
        // so we can abort old requests when a new one is make
        window.hinterXHR = new XMLHttpRequest();
      },
      
      methods: {
        hinter: function(event) {
        
        // retain access to the Vue instance
        var app = this
        
        // retireve the input element
        var input = event.target;
        
        // retrieve the datalist element
        var huge_list = this.$refs.huge_list
        
        // display new set of results for each query
        var results = this.$refs.results
        
        // minimum number of characters before we start to generate suggestions
        var min_characters = 3;
        
        if (input.value.length < min_characters ) { 
        
          app.responseData = [];
          return;
          
        } else { 
        
            // abort any pending requests
            window.hinterXHR.abort();
            
            window.hinterXHR.onreadystatechange = function() {
            
                if (this.readyState == 4 && this.status == 200) {
                
                    // We're expecting a json response so we convert it to an object
                    var response = JSON.parse( this.responseText ); 
                    
                    // clear any previously loaded options in the datalist and responseData array
                    huge_list.innerHTML = ""
                    app.responseData = response
                    
                    response.forEach(function(item) {
                        // Create a new <option> element.
                        var option = document.createElement('option');
                        option.value = item.name;
                        // attach the option to the datalist element
                        huge_list.appendChild(option);
                    });
                }
            };
            
            window.hinterXHR.open("GET", "/api/search?name=" + input.value, true);
            window.hinterXHR.send()
        }
    }
      }
    }
    
    </script>
    
    <style scoped>
    .list-results-container {
    margin: 2em 0 8em 0;
    }
    .list-results {
      padding: 0.5em;
    }
    .navbar-default .nav-large-font > li > a {
      color: #000;
      font-size: 1.0625em;
    }
    .navbar-transparent {
      background-color: transparent;
      border-bottom: none;
    }
    button.btn-sign-in {
      font-weight: bold;
      color: #fff;
      background-color: #4683ea;
    }
    .navbar-nav>li, .navbar-nav {
    float: left !important;
    }
    .navbar-nav.navbar-right:last-child {
    margin-right: -15px !important;
    }
    .navbar-right {
    float: right !important;
    }
    #google-logo {
      width: 272px;
      height: 92px;
    }
    /* FORM */
    .form-adjustment {
      margin-top: 5em;
    }
    #gg-search {
      width: 500px;
    }
    .input-group-addon-transparent {
      background-color: transparent;
    }
    /* BUTTONS */
    .button-adjustment {
      margin-top: 50px;
    }
    .button-adjustment button {
      background-color: #f2f2f2;
      color: #757575;
      font-family: arial, sans-serif;
      font-size: 13px;
      font-weight: bold;
    }
    
    
    @media (max-width: 300px) {
        .navbar.navbar-default.navbar-fixed-top {
            display: none;
        }
    }
    </style>