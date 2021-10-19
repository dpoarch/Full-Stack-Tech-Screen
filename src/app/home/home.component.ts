import { HttpClient } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';


@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})



export class HomeComponent implements OnInit {

  
  constructor(private http: HttpClient) { }
  images: any;

  ngOnInit(): void {
    this.getClient();
  }

  getClient(){
    let array = [];
    this.http.get<any>("http://127.0.0.1:4847/images").subscribe(res => {
      console.log(res.content);
      this.images = res.content;
      
      // for(var i = 0; i< this.images.length; i++){
      //   array.push(this.images[i].image_name);
        
      // }
    })
    
  }

}

export interface Images{
  image_name: string
}


