import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { CompanyListComponent } from './Company List/company-list.component';
import { CompanyPageComponent } from './Company Detail/company-page.component';
import {VacancyListComponent} from './vacancy-list/vacancy-list.component';
import {VacancyDetailComponent} from './vacancy-detail/vacancy-detail.component';


const routes: Routes = [
  { path: '', component: CompanyListComponent },
  { path: 'company/:id', component: CompanyPageComponent },
  { path: 'company/:id/vacancies', component: VacancyListComponent },
  { path: 'company/:id/vacancies/:vacancyId', component: VacancyDetailComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
