import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { SubscribeFormComponent } from './subscribe-form/subscribe-form.component';
import { ThankYouPageComponent } from './thank-you-page/thank-you-page.component';
import { GoodbyePageComponent } from './goodbye-page/goodbye-page.component';

@NgModule({
  declarations: [
    AppComponent,
    SubscribeFormComponent,
    ThankYouPageComponent,
    GoodbyePageComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    HttpClientModule,
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
