import { Component, OnInit } from '@angular/core';
import {CompanyService} from '../company.service';
import {Company} from '../Company';

@Component({
  selector: 'app-company-list',
  templateUrl: './company-list.component.html',
  styleUrls: ['./company-list.component.css']
})
export class CompanyListComponent implements OnInit {
  companies: Company[];
  constructor(
    private companyService: CompanyService,
  ) { }

  ngOnInit(): void {
    this.getCompanies();
  }
  getCompanies() {
    this.companyService.getCompanies().subscribe(companies => this.companies = companies);
  }

}
