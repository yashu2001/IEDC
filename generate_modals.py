template='''<!-- Modal {} starts -->
    <div
      class="modal fade bd-example-modal-lg"
      id="Modal{}"
      tabindex="-1"
      role="dialog"
      aria-hidden="true"
    >
      <div class="modal-dialog modal-lg" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <button
              type="button"
              class="close"
              data-dismiss="modal"
              aria-label="Close"
            >
              <span aria-hidden="true">×</span>
            </button>
          </div>
          <div class="modal-body">
            <div id="Carousel{}" class="carousel slide" data-ride="carousel">
              <div class="carousel-inner">
                <div class="carousel-item active">
                  <img
                    src="assets/images/projects/team 1/one.jpg"
                    alt=""
                    class="img-fluid"
                  />
                </div>
                <div class="carousel-item">
                  <img
                    src="assets/images/projects/team 1/two.jpg"
                    alt=""
                    class="img-fluid"
                  />
                </div>
              </div>
              <a
                class="carousel-control-prev"
                href="#Carousel{}"
                role="button"
                data-slide="prev"
              >
                <span
                  class="carousel-control-prev-icon"
                  aria-hidden="true"
                ></span>
                <span class="sr-only">Previous</span>
              </a>
              <a
                class="carousel-control-next"
                href="#Carousel{}"
                role="button"
                data-slide="next"
              >
                <span
                  class="carousel-control-next-icon"
                  aria-hidden="true"
                ></span>
                <span class="sr-only">Next</span>
              </a>
            </div>
          </div>

          <div class="modal-footer">
            <button
              type="button"
              class="btn btn-secondary"
              data-dismiss="modal"
            >
              Close
            </button>
          </div>
        </div>
      </div>
    </div>
    <!-- End of modal {} -->'''
s=''
for i in range(1,40):
    s+=template.format(i,i,i,i,i,i)
with open('modals.txt','w') as write_file:
    write_file.write(s)