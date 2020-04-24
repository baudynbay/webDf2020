import {Component, OnInit} from '@angular/core';
import {CompanyService} from '../company.service';
import {Company} from '../models';

@Component({
  selector: 'app-news-list',
  templateUrl: './company-list.html',
  styleUrls: ['./company-list.component.css']
})
export class CompanyListComponent implements OnInit {
  companies: Company[] = [];

  constructor(public categoryService: CompanyService) {
  }

  ngOnInit(): void {
    this.getCategoryList();
  }

  getCategoryList() {
    this.categoryService.getCategoryList()
      .subscribe(companies => {
        this.companies = companies;
      });
  }

  deleteCategory(id) {
    this.categoryService.deleteCategory(id).subscribe(res => {
      // this.categories = this.categories.filter(c => c.id != id);
      // this.getCategoryList();
    });
  }

}
