class RotatingContainer {
    constructor(lona_window) {
        this.lona_window = lona_window;
    }

    animate(time) {
        const container = this.root_node;

        this.angle = this.angle + 2;

        if(this.angle >= 360) {
            this.angle = 0;
        }

        container.style['transform'] = `rotate(${this.angle}deg)`;

        if(this.data['animation_running']) {
            requestAnimationFrame(time => {
                this.animate(time);
            });
        }
    }

    setup() {
        this.angle = 0;

        if(this.data['animation_running']) {
            requestAnimationFrame(time => {
                this.animate(time);
            });
        }
    }

    data_updated() {
        if(this.data['animation_running']) {
            requestAnimationFrame(time => {
                this.animate(time);
            });
        }
    }
}


Lona.register_widget_class('RotatingContainer', RotatingContainer);
