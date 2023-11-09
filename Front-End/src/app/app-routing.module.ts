import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ThankYouPageComponent } from './thank-you-page/thank-you-page.component';
import { GoodbyePageComponent } from './goodbye-page/goodbye-page.component';

const routes: Routes = [
  { path: 'thankyou', component: ThankYouPageComponent },
  { path: 'goodbye', component: GoodbyePageComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
