import {Component, Input, OnInit} from '@angular/core';
import {Vacancy} from '../Vacancy';
import {CompanyService} from '../company.service';
import {ActivatedRoute, Router} from '@angular/router';
import {Company} from '../Company';

@Component({
  selector: 'app-company-detail',
  templateUrl: './company-detail.component.html',
  styleUrls: ['./company-detail.component.css']
})
export class CompanyDetailComponent implements OnInit {
  @Input() company: Company;
  constructor(
    private router: Router,
    private companyService: CompanyService,
    private route: ActivatedRoute,
  ) { }

  ngOnInit(): void {
    this.getCompany();
  }

  getCompany() {
    const id = +this.route.snapshot.paramMap.get('id');
    this.companyService.getCompany(id)
      .subscribe(company => this.company = company);
  }
}
