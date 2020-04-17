import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppComponent } from './app.component';
import { CompanyListComponent } from './company-list/company-list.component';
import { CompanyDetailComponent } from './company-detail/company-detail.component';
import { VacancyListComponent } from './vacancy-list/vacancy-list.component';
import { RoutingModuleModule } from './routing-module.module';
import {HttpClientModule, HTTP_INTERCEPTORS} from '@angular/common/http';
import { LoginComponent } from './login/login.component';
import {FormsModule} from '@angular/forms';
import {AuthInterceptor} from './auth.interceptor';
import { CompanyVacanciesComponent } from './company-vacancies/company-vacancies.component';
import { VacancyDetailComponent } from './vacancy-detail/vacancy-detail.component';
@NgModule({
  declarations: [
    AppComponent,
    CompanyListComponent,
    CompanyDetailComponent,
    VacancyListComponent,
    LoginComponent,
    CompanyVacanciesComponent,
    VacancyDetailComponent
  ],
  imports: [
    BrowserModule,
    RoutingModuleModule,
    HttpClientModule,
    FormsModule,
  ],
  providers: [
    {
      provide: HTTP_INTERCEPTORS,
      useClass: AuthInterceptor,
      multi: true
    }
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
