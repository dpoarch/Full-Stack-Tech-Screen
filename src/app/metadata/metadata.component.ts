import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-metadata',
  templateUrl: './metadata.component.html',
  styleUrls: ['./metadata.component.css']
})
export class MetadataComponent implements OnInit {

  id: any;
  images: any;
  constructor(private _Activatedroute:ActivatedRoute, private http: HttpClient) {
    this.id = this._Activatedroute.snapshot.paramMap.get("id");
    console.log(this.id);
    this.getClient(this.id);
   }

  ngOnInit(): void {
  }

  getClient(id:any){
    let array = [];
    this.http.get<any>("http://127.0.0.1:4847/metadata/?image_name="+id).subscribe(res => {
      console.log(res);
      this.images = res.data;
      console.log(this.images);
      
      // for(var i = 0; i< this.images.length; i++){
      //   array.push(this.images[i].image_name);
        
      // }
    })
    
  }

}

export interface Images{
  image_name: string
}
