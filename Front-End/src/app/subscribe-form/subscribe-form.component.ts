import { Component } from '@angular/core';
import { NgForm } from '@angular/forms';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-subscribe-form',
  templateUrl: './subscribe-form.component.html',
  styleUrls: ['./subscribe-form.component.css']
})

export class SubscribeFormComponent {
  formData: any = {};
  constructor(private http: HttpClient) { } // Inject HttpClient

  onSubmit(form: NgForm) {
    if (form.valid) {

      // check to see if form was received
      console.log('Form Data:', this.formData);

      const topicCheckboxes = [
        this.formData.topic1, this.formData.topic2, this.formData.topic3, this.formData.topic4,
        this.formData.topic5, this.formData.topic6, this.formData.topic7, this.formData.topic8,
        this.formData.topic9, this.formData.topic10, this.formData.topic11, this.formData.topic12];
      const selectedTopics: number[] = [];

      topicCheckboxes.forEach((isChecked, index) => {
        if (isChecked) { selectedTopics.push(index + 1); }
      });
      console.log(selectedTopics);

      // create the request body
      const jsonData = {
        name: this.formData.name,
        email: this.formData.email,
        topics: selectedTopics,
      };
      console.log(jsonData)

      // Send the JSON data to an API endpoint
      this.http.post('http://localhost:5000/users/subscribe/', jsonData).subscribe(
        (response) => {
          // Handle the API response here
          console.log('API Response:', response);

          // Reset the form after submission
          form.resetForm();
        },
        (error) => {
          // Handle API error
          console.error('API Error:', error);
        }
      );
    }
  }
}
