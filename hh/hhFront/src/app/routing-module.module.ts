import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import {RouterModule, Routes} from '@angular/router';
import {CompanyListComponent} from './company-list/company-list.component';
import {CompanyDetailComponent} from './company-detail/company-detail.component';
import {VacancyListComponent} from './vacancy-list/vacancy-list.component';
import {LoginComponent} from './login/login.component';
import {CompanyVacanciesComponent} from './company-vacancies/company-vacancies.component';
import {VacancyDetailComponent} from './vacancy-detail/vacancy-detail.component';

const routes: Routes = [
  { path: '', redirectTo: 'login', pathMatch: 'full' },
  { path: 'companies', component: CompanyListComponent},
  { path: 'companies/:id', component: CompanyDetailComponent},
  {path: 'companies/:id/vacancies', component: CompanyVacanciesComponent},
  { path: 'vacancies', component: VacancyListComponent},
  { path: 'vacancies/:id', component: VacancyDetailComponent},
  { path: 'login', component: LoginComponent},
];

@NgModule({
  declarations: [],
  imports: [
    CommonModule,
    RouterModule.forRoot(routes)
  ],
  exports: [RouterModule]
})
export class RoutingModuleModule { }
