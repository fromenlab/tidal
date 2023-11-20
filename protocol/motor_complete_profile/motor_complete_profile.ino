
// Motor control parameters
// int (*p)[5][500];

// Maneuver arrays
const PROGMEM unsigned int identity[500] = {1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1};

const PROGMEM unsigned int stored_inhale[5][500] = {
  {2965, 1339, 945, 770, 672, 609, 566, 534, 509, 490, 474, 461, 450, 441, 433, 426, 420, 415, 411, 407, 403, 400, 398, 396, 393, 392, 390, 389, 388, 387, 386, 385, 385, 385, 384, 384, 384, 384, 384, 385, 385, 386, 386, 387, 387, 388, 389, 390, 391, 391, 393, 394, 395, 396, 397, 399, 400, 401, 403, 404, 406, 407, 409, 411, 412, 414, 416, 418, 420, 422, 424, 426, 428, 430, 433, 435, 437, 440, 442, 444, 447, 449, 452, 455, 458, 460, 463, 466, 469, 472, 475, 478, 481, 485, 488, 491, 495, 498, 502, 505, 509, 513, 517, 521, 525, 529, 533, 537, 542, 546, 550, 555, 560, 564, 569, 574, 579, 585, 590, 595, 601, 606, 612, 618, 624, 630, 636, 643, 649, 656, 663, 670, 677, 684, 692, 700, 708, 716, 724, 732, 741, 750, 759, 769, 778, 788, 798, 809, 819, 830, 842, 853, 865, 878, 891, 904, 917, 931, 946, 961, 976, 992, 1008, 1025, 1043, 1061, 1080, 1100, 1120, 1141, 1163, 1186, 1210, 1234, 1260, 1287, 1315, 1344, 1375, 1407, 1441, 1477, 1514, 1553, 1594, 1638, 1684, 1733, 1784, 1839, 1897, 1960, 2026, 2097, 2173, 2256, 2344, 2440, 2544, 2658},
  {730, 717, 705, 693, 683, 673, 664, 655, 646, 638, 631, 624, 618, 611, 605, 600, 595, 590, 585, 581, 576, 572, 569, 565, 562, 559, 556, 553, 550, 548, 545, 543, 541, 539, 537, 535, 534, 532, 531, 529, 528, 527, 526, 525, 524, 523, 522, 521, 520, 519, 518, 518, 517, 516, 515, 515, 514, 513, 513, 512, 511, 511, 510, 509, 509, 508, 507, 506, 505, 505, 504, 503, 502, 501, 500, 499, 498, 497, 496, 495, 494, 492, 491, 490, 489, 487, 486, 485, 483, 482, 481, 479, 478, 476, 475, 473, 471, 470, 468, 467, 465, 463, 462, 460, 459, 457, 455, 454, 452, 450, 449, 447, 446, 444, 442, 441, 439, 438, 436, 435, 433, 432, 430, 429, 427, 426, 424, 423, 421, 420, 419, 417, 416, 415, 414, 412, 411, 410, 409, 408, 406, 405, 404, 403, 402, 401, 400, 399, 398, 397, 397, 396, 395, 394, 393, 393, 392, 391, 390, 390, 389, 389, 388, 387, 387, 386, 386, 385, 385, 385, 384, 384, 383, 383, 383, 383, 382, 382, 382, 382, 382, 381, 381, 381, 381, 381, 381, 381, 381, 381, 381, 381, 382, 382, 382, 382, 382, 383, 383, 383},
  {612, 599, 587, 575, 565, 555, 546, 537, 529, 522, 515, 508, 502, 496, 490, 485, 480, 475, 471, 466, 462, 458, 455, 451, 448, 445, 442, 439, 436, 434, 431, 429, 427, 425, 423, 421, 419, 418, 416, 415, 413, 412, 411, 410, 409, 408, 407, 406, 405, 405, 404, 403, 403, 402, 402, 402, 401, 401, 401, 401, 401, 401, 401, 401, 401, 402, 402, 402, 403, 403, 404, 404, 405, 405, 406, 407, 408, 408, 409, 410, 411, 412, 413, 414, 416, 417, 418, 419, 421, 422, 423, 425, 426, 428, 430, 431, 433, 435, 436, 438, 440, 442, 444, 446, 448, 450, 452, 454, 457, 459, 461, 463, 466, 468, 470, 473, 475, 478, 480, 483, 485, 488, 490, 493, 496, 498, 501, 503, 506, 509, 511, 514, 517, 519, 522, 524, 527, 530, 532, 535, 537, 539, 542, 544, 546, 549, 551, 553, 555, 557, 559, 561, 563, 564, 566, 568, 569, 570, 572, 573, 574, 575, 576, 577, 578, 578, 579, 579, 580, 580, 580, 580, 580, 580, 579, 579, 579, 578, 577, 577, 576, 575, 574, 573, 571, 570, 569, 567, 566, 564, 562, 560, 559, 557, 555, 553, 550, 548, 546, 544},
  {895, 857, 822, 791, 763, 737, 713, 692, 672, 655, 638, 623, 610, 597, 586, 575, 565, 556, 548, 541, 534, 528, 522, 517, 512, 508, 504, 500, 497, 494, 491, 489, 487, 485, 483, 482, 480, 479, 478, 477, 476, 476, 475, 475, 474, 474, 474, 474, 474, 474, 474, 474, 474, 474, 474, 474, 475, 475, 475, 476, 476, 476, 476, 477, 477, 477, 478, 478, 478, 479, 479, 479, 480, 480, 480, 480, 480, 481, 481, 481, 481, 481, 481, 481, 481, 481, 481, 481, 481, 481, 481, 481, 481, 481, 480, 480, 480, 480, 479, 479, 479, 478, 478, 478, 477, 477, 476, 476, 475, 475, 474, 474, 473, 473, 472, 472, 471, 470, 470, 469, 469, 468, 468, 467, 467, 466, 466, 465, 465, 464, 464, 463, 463, 463, 462, 462, 462, 461, 461, 461, 461, 461, 461, 461, 461, 461, 461, 461, 462, 462, 462, 463, 463, 464, 464, 465, 466, 467, 468, 469, 470, 471, 472, 474, 475, 476, 478, 480, 482, 483, 485, 488, 490, 492, 494, 497, 500, 502, 505, 508, 511, 515, 518, 522, 525, 529, 533, 537, 542, 546, 551, 556, 561, 566, 571, 577, 582, 589, 595, 601},
  {635, 646, 656, 663, 669, 674, 678, 681, 683, 685, 686, 687, 687, 686, 686, 685, 683, 682, 680, 678, 676, 674, 671, 669, 666, 664, 661, 658, 655, 652, 650, 647, 644, 641, 638, 635, 632, 629, 626, 623, 620, 617, 614, 611, 608, 605, 603, 600, 597, 595, 592, 590, 587, 585, 582, 580, 577, 575, 573, 571, 568, 566, 564, 562, 560, 558, 557, 555, 553, 551, 550, 548, 546, 545, 543, 542, 540, 539, 538, 537, 535, 534, 533, 532, 531, 530, 529, 528, 527, 526, 525, 525, 524, 523, 523, 522, 522, 521, 521, 520, 520, 519, 519, 519, 519, 518, 518, 518, 518, 518, 518, 518, 518, 518, 518, 519, 519, 519, 519, 520, 520, 520, 521, 521, 522, 522, 523, 523, 524, 525, 525, 526, 527, 528, 529, 530, 531, 532, 533, 534, 535, 536, 537, 538, 540, 541, 543, 544, 546, 547, 549, 551, 552, 554, 556, 558, 560, 563, 565, 567, 570, 572, 575, 577, 580, 583, 586, 590, 593, 597, 600, 604, 608, 612, 617, 622, 627, 632, 637, 643, 649, 656, 663, 670, 678, 687, 696, 705, 716, 727, 739, 752, 767, 783, 801, 820, 842, 867, 895, 928}
  };

const PROGMEM unsigned int stored_exhale[5][500] = {
  {372, 383, 392, 400, 408, 415, 422, 428, 433, 439, 444, 449, 453, 458, 462, 466, 469, 473, 476, 480, 483, 486, 489, 491, 494, 496, 499, 501, 503, 505, 507, 509, 511, 513, 514, 516, 517, 519, 520, 521, 522, 524, 525, 526, 527, 528, 528, 529, 530, 531, 531, 532, 533, 533, 534, 534, 534, 535, 535, 536, 536, 536, 536, 537, 537, 537, 537, 537, 538, 538, 538, 538, 538, 538, 538, 538, 538, 538, 538, 538, 538, 538, 538, 538, 538, 538, 538, 538, 538, 538, 538, 538, 538, 538, 537, 537, 537, 537, 537, 537, 537, 537, 538, 538, 538, 538, 538, 538, 538, 538, 538, 538, 539, 539, 539, 539, 540, 540, 540, 540, 541, 541, 542, 542, 543, 543, 544, 544, 545, 545, 546, 547, 548, 548, 549, 550, 551, 552, 553, 554, 555, 556, 557, 559, 560, 561, 563, 564, 566, 568, 570, 571, 573, 575, 577, 580, 582, 584, 587, 589, 592, 595, 598, 601, 604, 607, 611, 615, 619, 623, 627, 631, 636, 641, 646, 652, 657, 663, 670, 676, 683, 691, 699, 707, 716, 726, 736, 746, 758, 770, 783, 797, 812, 829, 846, 866, 887, 910, 935, 962},
  {350, 364, 374, 382, 389, 394, 399, 404, 408, 412, 415, 418, 421, 424, 426, 428, 431, 433, 434, 436, 438, 439, 441, 442, 443, 444, 445, 446, 447, 448, 449, 450, 450, 451, 452, 452, 453, 453, 454, 454, 455, 455, 456, 456, 457, 457, 457, 458, 458, 458, 458, 459, 459, 459, 459, 460, 460, 460, 460, 461, 461, 461, 461, 461, 462, 462, 462, 462, 463, 463, 463, 463, 464, 464, 464, 465, 465, 465, 465, 466, 466, 466, 467, 467, 468, 468, 468, 469, 469, 470, 470, 471, 471, 472, 472, 473, 473, 474, 474, 475, 476, 476, 477, 478, 478, 479, 480, 480, 481, 482, 483, 484, 485, 485, 486, 487, 488, 489, 490, 491, 492, 493, 494, 495, 497, 498, 499, 500, 501, 503, 504, 505, 506, 508, 509, 511, 512, 513, 515, 516, 518, 519, 521, 523, 524, 526, 528, 529, 531, 533, 535, 536, 538, 540, 542, 544, 545, 547, 549, 551, 553, 555, 557, 559, 561, 563, 565, 566, 568, 570, 572, 574, 575, 577, 579, 580, 582, 583, 585, 586, 587, 588, 589, 590, 590, 591, 591, 591, 591, 590, 589, 588, 587, 585, 583, 580, 577, 574, 569, 565},
  {350, 355, 360, 365, 370, 375, 380, 385, 390, 396, 401, 406, 412, 417, 423, 428, 434, 439, 445, 451, 456, 462, 468, 473, 479, 485, 491, 496, 502, 507, 513, 519, 524, 529, 535, 540, 545, 550, 555, 560, 565, 569, 573, 578, 582, 586, 589, 593, 596, 599, 602, 604, 607, 609, 611, 612, 614, 615, 616, 616, 616, 616, 616, 616, 615, 614, 612, 611, 609, 607, 605, 603, 600, 597, 594, 591, 588, 585, 581, 577, 574, 570, 566, 562, 558, 555, 551, 547, 543, 539, 535, 531, 528, 524, 521, 517, 514, 511, 507, 504, 501, 499, 496, 493, 491, 489, 486, 484, 482, 481, 479, 477, 476, 475, 474, 473, 472, 471, 470, 470, 469, 469, 469, 469, 469, 469, 470, 470, 471, 472, 472, 473, 474, 476, 477, 478, 480, 482, 483, 485, 487, 490, 492, 494, 497, 500, 503, 506, 509, 512, 516, 519, 523, 527, 531, 536, 540, 545, 550, 555, 560, 566, 572, 578, 584, 591, 598, 605, 613, 621, 629, 638, 647, 657, 667, 678, 689, 701, 713, 726, 740, 755, 770, 787, 805, 823, 843, 865, 888, 913, 940, 969, 1001, 1035, 1073, 1115, 1162, 1214, 1273, 1339},
  {768, 750, 732, 716, 700, 685, 671, 657, 645, 632, 620, 609, 599, 589, 579, 570, 561, 552, 544, 537, 530, 523, 516, 510, 504, 498, 492, 487, 482, 478, 473, 469, 464, 461, 457, 453, 450, 446, 443, 440, 437, 435, 432, 429, 427, 425, 422, 420, 418, 416, 414, 413, 411, 409, 408, 406, 405, 403, 402, 401, 400, 399, 397, 396, 395, 395, 394, 393, 392, 391, 390, 390, 389, 389, 388, 387, 387, 386, 386, 386, 385, 385, 385, 384, 384, 384, 384, 384, 383, 383, 383, 383, 383, 383, 383, 383, 383, 384, 384, 384, 384, 384, 385, 385, 385, 385, 386, 386, 387, 387, 387, 388, 388, 389, 390, 390, 391, 391, 392, 393, 393, 394, 395, 396, 397, 398, 398, 399, 400, 401, 402, 403, 405, 406, 407, 408, 409, 411, 412, 413, 415, 416, 418, 419, 421, 423, 424, 426, 428, 430, 432, 434, 436, 438, 440, 442, 445, 447, 450, 452, 455, 458, 460, 463, 466, 470, 473, 476, 480, 483, 487, 491, 495, 500, 504, 509, 514, 519, 524, 530, 536, 542, 548, 555, 562, 570, 578, 587, 596, 605, 616, 627, 639, 652, 667, 682, 699, 718, 739, 762},
  {740, 709, 681, 658, 637, 618, 602, 587, 574, 561, 550, 540, 530, 522, 513, 506, 499, 492, 486, 480, 475, 470, 465, 460, 456, 452, 448, 444, 440, 437, 434, 431, 428, 425, 422, 420, 417, 415, 413, 411, 409, 407, 405, 403, 401, 400, 398, 397, 395, 394, 392, 391, 390, 389, 388, 387, 386, 385, 384, 383, 382, 381, 381, 380, 379, 379, 378, 377, 377, 376, 376, 375, 375, 375, 374, 374, 374, 374, 373, 373, 373, 373, 373, 373, 373, 373, 373, 373, 373, 373, 373, 373, 373, 373, 374, 374, 374, 374, 375, 375, 375, 376, 376, 377, 377, 378, 378, 379, 379, 380, 381, 381, 382, 383, 384, 384, 385, 386, 387, 388, 389, 390, 391, 392, 393, 394, 395, 397, 398, 399, 400, 402, 403, 405, 406, 408, 409, 411, 413, 414, 416, 418, 420, 422, 424, 426, 428, 430, 433, 435, 438, 440, 443, 446, 448, 451, 454, 457, 461, 464, 467, 471, 475, 479, 483, 487, 491, 496, 500, 505, 510, 516, 521, 527, 533, 539, 546, 553, 561, 568, 577, 585, 595, 604, 615, 626, 638, 651, 664, 679, 695, 713, 732, 753, 776, 802, 831, 864, 901, 945}
  };

#define idarr {1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1}
#define idarr1000 {1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000}

unsigned int delays[][500] = {
  idarr1000,
  idarr1000,
  idarr1000,
  idarr1000,
  idarr1000
};

// Default parameters
int inhale = 1;
int exhale = -1;

#define NUM_STEPPERS 5
int rul = 0;
int rml = 1;
int rll = 2;
int lul = 3;
int lll = 4;

#define RUL_DIR_PIN          36
#define RUL_STEP_PIN         37

#define RML_DIR_PIN          40
#define RML_STEP_PIN         41

#define RLL_DIR_PIN          44
#define RLL_STEP_PIN         45

#define LUL_DIR_PIN          48
#define LUL_STEP_PIN         49

#define LLL_DIR_PIN          52
#define LLL_STEP_PIN         53

#define RUL_STEP_HIGH             PORTC |=  0b00000001;
#define RUL_STEP_LOW              PORTC &= ~0b00000001;

#define RML_STEP_HIGH             PORTG |=  0b00000001;
#define RML_STEP_LOW              PORTG &= ~0b00000001;

#define RLL_STEP_HIGH             PORTL |=  0b00010000;
#define RLL_STEP_LOW              PORTL &= ~0b00010000;

#define LUL_STEP_HIGH             PORTL |=  0b00000001;
#define LUL_STEP_LOW              PORTL &= ~0b00000001;

#define LLL_STEP_HIGH             PORTB |=  0b00000001;
#define LLL_STEP_LOW              PORTB &= ~0b00000001;



#define TIMER1_INTERRUPTS_ON    TIMSK1 |=  (1 << OCIE1A);
#define TIMER1_INTERRUPTS_OFF   TIMSK1 &= ~(1 << OCIE1A);

struct stepperInfo {
  // Lobe-specific parameters
  void (*dirFunc)(int);
  void (*stepFunc)();
  volatile int uml;                        // upper(0), middle(1), or lower(2) position
  volatile unsigned int default_steps = 100;
  volatile unsigned int default_delay = 2000;

  // derived parameters
  long stepPosition;              // current position of stepper (total of all movements taken so far)

  // per movement variables (only changed once per movement)
  volatile int dir;                        // current direction of movement, used to keep track of position
  volatile unsigned int totalSteps;        // number of steps requested for current movement
  volatile bool movementDone = false;      // true if the current movement has been completed (used by main program to wait for completion)

  // per iteration variables (potentially changed every interrupt)
  volatile float d;                        // current interval length
  volatile unsigned long di;               // above variable truncated
  volatile unsigned int stepCount;         // number of steps completed in current movement

};

void rulStep() {
  RUL_STEP_HIGH
delayMicroseconds(10);
  RUL_STEP_LOW
delayMicroseconds(10);
}
void rulDir(int dir) {
  dir = dir == LOW ? HIGH : LOW;
  digitalWrite(RUL_DIR_PIN, dir);
}

void rmlStep() {
  RML_STEP_HIGH
delayMicroseconds(10);
  RML_STEP_LOW
delayMicroseconds(10);
}
void rmlDir(int dir) {
  digitalWrite(RML_DIR_PIN, dir);
}

void rllStep() {
  RLL_STEP_HIGH
delayMicroseconds(10);
  RLL_STEP_LOW
delayMicroseconds(10);
}
void rllDir(int dir) {
  dir = dir == LOW ? HIGH : LOW;
  digitalWrite(RLL_DIR_PIN, dir);
}

void lulStep() {
  LUL_STEP_HIGH
delayMicroseconds(10);
  LUL_STEP_LOW
delayMicroseconds(10);
}
void lulDir(int dir) {
  digitalWrite(LUL_DIR_PIN, dir);
}

void lllStep() {
  LLL_STEP_HIGH
delayMicroseconds(10);
  LLL_STEP_LOW
delayMicroseconds(10);
}
void lllDir(int dir) {
  digitalWrite(LLL_DIR_PIN, dir);
}

void resetStepperInfo( stepperInfo& si ) {
  si.d = 0;
  si.di = 0;
  si.stepCount = 0;
  si.totalSteps = 0;
  si.stepPosition = 0;
  si.movementDone = false;
}

volatile stepperInfo steppers[NUM_STEPPERS];

void setup() {

  Serial.begin(19200);
  Serial.flush();
  pinMode(LED_BUILTIN, OUTPUT);

  pinMode(RUL_STEP_PIN,   OUTPUT);
  pinMode(RUL_DIR_PIN,    OUTPUT);

  pinMode(RML_STEP_PIN,   OUTPUT);
  pinMode(RML_DIR_PIN,    OUTPUT);

  pinMode(RLL_STEP_PIN,   OUTPUT);
  pinMode(RLL_DIR_PIN,    OUTPUT);

  pinMode(LUL_STEP_PIN,   OUTPUT);
  pinMode(LUL_DIR_PIN,    OUTPUT);

  pinMode(LLL_STEP_PIN,   OUTPUT);
  pinMode(LLL_DIR_PIN,    OUTPUT);


  noInterrupts();
  TCCR1A = 0;
  TCCR1B = 0;
  TCNT1  = 0;

  OCR1A = 1000;                             // compare value
  TCCR1B |= (1 << WGM12);                   // CTC mode
  TCCR1B |= ((1 << CS11) | (1 << CS10));    // 64 prescaler
  interrupts();

  steppers[rul].dirFunc = rulDir;
  steppers[rul].stepFunc = rulStep;
  steppers[rul].uml = 0;

  steppers[rml].dirFunc = rmlDir;
  steppers[rml].stepFunc = rmlStep;
  steppers[rml].uml = 1;

  steppers[rll].dirFunc = rllDir;
  steppers[rll].stepFunc = rllStep;
  steppers[rll].uml = 2;

  steppers[lul].dirFunc = lulDir;
  steppers[lul].stepFunc = lulStep;
  steppers[lul].uml = 0;

  steppers[lll].dirFunc = lllDir;
  steppers[lll].stepFunc = lllStep;
  steppers[lll].uml = 2;
}

void resetStepper(volatile stepperInfo& si) {
  si.di = si.d;
  si.stepCount = 0;
  si.movementDone = false;
}

volatile byte remainingSteppersFlag = 0;

void prepareMovement(int whichMotor, int steps) {
  volatile stepperInfo& si = steppers[whichMotor];
  si.dirFunc( steps < 0 ? HIGH : LOW );
  si.dir = steps > 0 ? 1 : -1;
  si.totalSteps = abs(steps);
  resetStepper(si);
  remainingSteppersFlag |= (1 << whichMotor);
}

volatile byte nextStepperFlag = 0;

void setNextInterruptInterval() {

    // Serial.println(remainingSteppersFlag, BIN);

  unsigned int mind = 65535;
  for (int i = 0; i < NUM_STEPPERS; i++) {
    if ( ((1 << i) & remainingSteppersFlag) && steppers[i].di < mind ) {
      mind = steppers[i].di;
    }
  }

  nextStepperFlag = 0;
  for (int i = 0; i < NUM_STEPPERS; i++) {
    if ( ((1 << i) & remainingSteppersFlag) && steppers[i].di == mind )
      nextStepperFlag |= (1 << i);
  }

  OCR1A = mind;

  // Serial.print(F("OCR1A: "));
  // Serial.println(OCR1A);
}

ISR(TIMER1_COMPA_vect)
{
  // Serial.println(TCNT1);
  unsigned int tmpCtr = OCR1A;

  OCR1A = 65535;
  

  for (int i = 0; i < NUM_STEPPERS; i++) {

    if ( ! ((1 << i) & remainingSteppersFlag) )
      continue;

    if ( ! (nextStepperFlag & (1 << i)) ) {
      steppers[i].di -= tmpCtr;
      continue;
    }

    volatile stepperInfo& s = steppers[i];

    if ( s.stepCount < s.totalSteps ) {
      s.stepFunc();
      s.stepCount++;
      s.stepPosition += s.dir;
      // s.d = p[0][s.uml][s.stepCount];
      s.d = delays[i][s.stepCount];
      if ( s.stepCount >= s.totalSteps ) {
        s.movementDone = true;
        remainingSteppersFlag &= ~(1 << i);
      }
    }

    s.di = s.d; // Set integer delay
//    Serial.println(s.di);
//    Serial.println(s.stepCount);
  }
  setNextInterruptInterval();
  // Serial.println(TCNT1);
  TCNT1  = 0; // The timer continues to run during the ISR and movements. Set to 0 in case time is passed
}

void runAndWait() {
  // Serial.println("Begin run");
  noInterrupts();
  OCR1A = 65535;
  TCNT1 = 0;
  interrupts();
  setNextInterruptInterval();
  TIMER1_INTERRUPTS_ON
  while ( remainingSteppersFlag ); // Wait until motion is finished
  TIMER1_INTERRUPTS_OFF
//   setNextInterruptInterval();
}


//============
// Serial processing variables
const byte numChars = 32;
char receivedChars[numChars];
char tempChars[numChars];        // temporary array for use when parsing
boolean newData = false;

// Mutable parameters
float DELAY_PROFILE = 0.1;
int PROFILE_CYCLES = 5;
float DELAY_INHALE = 0.1;
float DELAY_EXHALE = 0.1;
int START_MANEUVER = exhale;



void recvWithStartEndMarkers() {
    static boolean recvInProgress = false;
    static byte ndx = 0;
    char startMarker = '<';
    char endMarker = '>';
    char rc;

    while (Serial.available() > 0 && newData == false) {
        rc = Serial.read();

        if (recvInProgress == true) {
            if (rc != endMarker) {
                receivedChars[ndx] = rc;
                ndx++;
                if (ndx >= numChars) {
                    ndx = numChars - 1;
                }
            }
            else {
                receivedChars[ndx] = '\0'; // terminate the string
                recvInProgress = false;
                ndx = 0;
                newData = true;
            }
        }

        else if (rc == startMarker) {
            recvInProgress = true;
        }
    }
}

//============

#define SEP "/"

void checkType() {
    // Serial.print(F("tempChars: "));
    // Serial.println(tempChars);
    switch (tempChars[0])
    {
    case '?':
        parseQuery();
        break;
    case 'S':
        parseS();
        break;
    case 'R':
        if (strcmp(tempChars, "RUN") == 0)
        {
            // runAndWait();
            // if (!RUN) {
            //     RUN = true;
            // } else {
            //     RUN = false;
            // }
            runAndWait();
        } else
        {
            printInvalid();
        }
        break;
    case 'P':
        if (strcmp(tempChars, "PROFILEC") == 0)
        {
            run_profile_constant();
        } else if (strcmp(tempChars, "PROFILEV") == 0) {
            run_profile_variable();
        } else
        {
            printInvalid();
        }
        break;
    case 'C':
        parseC();
        break;
    default:
        printInvalid();
        break;
    }
}

void parseQuery() {
    // if (strcmp(tempChars, "?") == 0)
    // {
    //     Serial.println(F("OK"));
    // }
    if (true)
    {
      switch (tempChars[1]) {
        case '\0':
          Serial.println("OK");
          break;
        case 'S':
        printParams();
        break;
        case 'A':
        printDelays();
        break;
        default:
        printInvalid();
        break;
      }
    }
}

void parseS() {
    // Input: S{Setting}/{Value}/{Additional parameters}

    char * strtokIndx;

    char setting[10];
    float val = 0;

    strtokIndx = strtok(tempChars, SEP);
    strcpy(setting, strtokIndx);

    strtokIndx = strtok(NULL, SEP); // this continues where the previous call left off
    val = atof(strtokIndx); 

    switch (setting[1])
    {
    case 'A':
      switch (setting[2]) {
        case 'I':
            parseSAI();
            break;
        case 'C':
            parseSAC();
            break;
      }
      break;
    case 'D':
        switch (setting[2])
        {
        case 'I':
            DELAY_INHALE = val;
            break;
        case 'E':
            DELAY_EXHALE = val;
            break;
        case 'P':
            DELAY_PROFILE = val;
            break;
        }
        break;
    case 'L':
        parseSL();
        break;
    case 'M':
        parseSM();
        break;
    case 'N':
        // Set the number of breathing cycles
        PROFILE_CYCLES = val;
        break;
    case 'O':
        switch (setting[2])
        {
        case 'I':
            START_MANEUVER = inhale;
            break;
        case 'E':
            START_MANEUVER = exhale;
            break;
        }
        break;
    default:
        printInvalid();
        return;
    }
}

void parseSL() {
  // Input: SL{Setting}/{Value}/{Additional parameters}
  // Set lobe-specific parameters

  strcpy(tempChars, receivedChars);

    char * strtokIndx;

    char setting[10];
    char motors[5];
    unsigned int val = 0;

    strtokIndx = strtok(tempChars, SEP);
    strcpy(setting, strtokIndx);

    strtokIndx = strtok(NULL, SEP); // this continues where the previous call left off
    val = atoi(strtokIndx); 

    strtokIndx = strtok(NULL, SEP); // this continues where the previous call left off
    strcpy(motors, strtokIndx); 

    switch (setting[2])
    {
    case 'S':
        // Set steps
        for (size_t i = 0; i < 5; i++)
        {
            if (motors[i] == '1')
            {
                steppers[i].default_steps = val;
            }
            else
            {
                Serial.print(i);
                Serial.print(F(": "));
                Serial.println(F("Not set"));
            }
            
        }
        break;

    case 'D':
        // Set delays
        for (size_t i = 0; i < 5; i++)
        {
            if (motors[i] == '1')
            {
                steppers[i].default_delay = val;
            }
            else
            {
                Serial.print(i);
                Serial.print(F(": "));
                Serial.println(F("Not set"));
            }
            
        }
        break;
    
    default:
        printInvalid();
        return;
    }

}

void parseSM() {
    // Input: SM{Maneuver}/{Steps}/{Motors}

    strcpy(tempChars, receivedChars);

    char * strtokIndx;

    char setting[10];
    char motors[5];
    int val = 0;
    int maneuver;

    strtokIndx = strtok(tempChars, SEP);
    strcpy(setting, strtokIndx);

    strtokIndx = strtok(NULL, SEP); // this continues where the previous call left off
    val = atoi(strtokIndx); 

    strtokIndx = strtok(NULL, SEP); // this continues where the previous call left off
    strcpy(motors, strtokIndx); 

    switch (setting[2])
    {
    case 'I':
        maneuver = inhale;
        break;

    case 'E':
        maneuver = exhale;
        break;
    
    default:
        printInvalid();
        return;
    }

    for (size_t i = 0; i < 5; i++)
    {
        if (motors[i] == '1')
        {
            prepareM(i, maneuver*val);
        }
        else
        {
            Serial.print(i);
            Serial.print(F(": "));
            Serial.println(F("Not set"));
        }
        
    }

}

void parseSAI() {
    // Write
    // Input: SAI/{Index}/{Value}/{Motors}
    // Index: 0 - 500
    // Value: 0 - 65535
    // Motors: xxxxx

    strcpy(tempChars, receivedChars);

    char * strtokIndx;

    char setting[10];
    unsigned int index = 0;
    unsigned int val = 0;
    char motors[5];

    strtokIndx = strtok(tempChars, SEP);
    strcpy(setting, strtokIndx);

    strtokIndx = strtok(NULL, SEP); // this continues where the previous call left off
    index = atoi(strtokIndx); 

    strtokIndx = strtok(NULL, SEP); // this continues where the previous call left off
    val = atoi(strtokIndx); 

    strtokIndx = strtok(NULL, SEP); // this continues where the previous call left off
    strcpy(motors, strtokIndx);

    // Serial.print("Setting: ");
    // Serial.println(setting);

    // Serial.print("Index: ");
    // Serial.println(index);

    // Serial.print("Value: ");
    // Serial.println(val);

    // Serial.print("Motors: ");
    // Serial.println(motors);

    for (size_t i = 0; i < 5; i++)
    {
        if (motors[i] == '1')
        {
            delays[i][index] = val;
        }
        
    }
    
    for (size_t i = 0; i < 5; i++)
    {
        if (motors[i] == '1')
        {
            if (delays[i][index] == val) {
                Serial.println("OK");
            } else {
                Serial.println("Error");
            }
        }
        
    }

}

void parseSAC() {
    // Write
    // Input: SAC/{Value}/{Motors}
    // Value: 0 - 65535
    // Motors: xxxxx

    strcpy(tempChars, receivedChars);

    char * strtokIndx;

    char setting[10];
    unsigned int val = 0;
    char motors[5];

    strtokIndx = strtok(tempChars, SEP);
    strcpy(setting, strtokIndx);

    strtokIndx = strtok(NULL, SEP); // this continues where the previous call left off
    val = atoi(strtokIndx); 

    strtokIndx = strtok(NULL, SEP); // this continues where the previous call left off
    strcpy(motors, strtokIndx);

    if (val == 0 && motors[0] == '\0')
    // Use default values for all lobes
    {
        for (size_t i = 0; i < 5; i++)
        {
            for (size_t j = 0; j < 500; j++)
            {
                delays[i][j] = steppers[i].default_delay;
            }
        }
    }
    else
    {
      // Use specified value for given lobes
        for (size_t i = 0; i < 5; i++)
        {
            if (motors[i] == '1')
            {
                for (size_t j = 0; j < 500; j++)
                {
                    delays[i][j] = val;
                }
            }
        }
    }
}

void parseC() {
    // Write
    // Input: C{Maneuver}/{Steps}/{Value}/{Motors}
    // Index: 0 - 500
    // Value: 0 - 65535
    // Motors: xxxxx

    char * strtokIndx;

    char setting[15];
    unsigned int index = 0;
    unsigned int val = 0;
    char motors[5];

    strtokIndx = strtok(tempChars, SEP);
    strcpy(setting, strtokIndx);

    strtokIndx = strtok(NULL, SEP); // this continues where the previous call left off
    index = atoi(strtokIndx); 

    strtokIndx = strtok(NULL, SEP); // this continues where the previous call left off
    val = atoi(strtokIndx); 

    strtokIndx = strtok(NULL, SEP); // this continues where the previous call left off
    strcpy(motors, strtokIndx);

    // Serial.print("Setting: ");
    // Serial.println(setting);

    // Serial.print("Index: ");
    // Serial.println(index);

    // Serial.print("Value: ");
    // Serial.println(val);

    // Serial.print("Motors: ");
    // Serial.println(motors);

    for (size_t i = 0; i < 5; i++)
    {
        if (motors[i] == '1')
        {
          for (size_t j = 0; j < index; j++)
          {
            delays[i][j] = val;
          }
        }
        
    }

    Serial.println("OK");
    
}

void prepareM(int i, int steps) {
    // Serial.print(i);
    // Serial.print(F(": "));
    // Serial.print(steps);
    // Serial.println(" steps");
    prepareMovement(i, steps);
}

void prepare_delays_constant() {
    // Set delays to default for each motor
    for (size_t i = 0; i < 5; i++)
        {
            for (size_t j = 0; j < 500; j++)
            {
                delays[i][j] = steppers[i].default_delay;
            }
        }
}

void run_profile_constant() {
prepare_delays_constant();
    delay(DELAY_PROFILE * 1000);

    for (int n = 0; n < PROFILE_CYCLES; n++)
    {
        // First breath maneuver
        for (int i = 0; i < 5; i++)
        {
            prepareM(i, START_MANEUVER * steppers[i].default_steps);
        }
        delay(DELAY_INHALE * 1000);
        runAndWait();

        // Second breath maneuver
        for (int i = 0; i < 5; i++)
        {
            prepareM(i, START_MANEUVER * -1 * steppers[i].default_steps);
        }
        delay(DELAY_EXHALE * 1000);
        runAndWait();
    }
}

    // Example of reading from progmem
    // unsigned int displayInt;
    // displayInt = pgm_read_word_near(&(stored_inhale[whichMotor][k]));
    // delays[whichMotor][k] = displayInt;
    // Serial.print(displayInt);
    // Serial.print(',');

void prepare_delays_variable(int maneuver) {
    if (maneuver == inhale) {
        for (int whichMotor = 0; whichMotor < 5; whichMotor ++) {
            for (int k = 0; k < 500; k++) {
                delays[whichMotor][k] = pgm_read_word_near(&(stored_inhale[whichMotor][k]));
            }
        }
    } else {
        for (int whichMotor = 0; whichMotor < 5; whichMotor ++) {
            for (int k = 0; k < 500; k++) {
                delays[whichMotor][k] = pgm_read_word_near(&(stored_exhale[whichMotor][k]));
            }
        }
    }
}

void run_profile_variable() {
    // Delay profile time
    delay(DELAY_PROFILE * 1000);
    // for number of breath cycles
    for (int n = 0; n < PROFILE_CYCLES; n++) {
        // Prepare first movement delays
        prepare_delays_variable(START_MANEUVER);

        // Prepare first movement
        for (int i = 0; i < 5; i++)
        {
            prepareM(i, START_MANEUVER * steppers[i].default_steps);
        }
        // First movement (inhale) delay period
        delay(DELAY_INHALE * 1000);
        runAndWait();

        // Prepare second movement delays
        prepare_delays_variable(START_MANEUVER*-1);
        for (int i = 0; i < 5; i++)
        {
            prepareM(i, START_MANEUVER * -1 * steppers[i].default_steps);
        }
        // Second movement delay period
        delay(DELAY_EXHALE * 1000);
        runAndWait();
    }
}

void printInvalid() {
    Serial.println(F("Invalid command"));
}

void printDelays() {
    Serial.println(F("Current delays:"));
  for (size_t i = 0; i < 5; i++)
        {
          Serial.print(F("Lobe "));
          Serial.print(i);
          Serial.print(F(": {"));
            for (size_t j = 0; j < 500; j++)
            {
                Serial.print(delays[i][j]);
                Serial.print(F(","));
            }
            Serial.println("}");
        }
        Serial.println(F("Stored inhale delays:"));
        for (int whichMotor = 0; whichMotor < 5; whichMotor ++) {
            Serial.print(F("Lobe "));
            Serial.print(whichMotor);
            Serial.print(F(": {"));
            for (int k = 0; k < 500; k++) {
                Serial.print(pgm_read_word_near(&(stored_inhale[whichMotor][k])));
                Serial.print(F(","));
            }
            Serial.println("}");
        }
        Serial.println(F("Stored exhale delays:"));
        for (int whichMotor = 0; whichMotor < 5; whichMotor ++) {
            Serial.print(F("Lobe "));
            Serial.print(whichMotor);
            Serial.print(F(": {"));
            for (int k = 0; k < 500; k++) {
                Serial.print(pgm_read_word_near(&(stored_exhale[whichMotor][k])));
                Serial.print(F(","));
            }
            Serial.println("}");
        }
}

void printParams() {
    Serial.print(F("Delay profile (s): "));
    Serial.println(DELAY_PROFILE);

    Serial.print(F("Profile cycles: "));
    Serial.println(PROFILE_CYCLES);

    for (size_t i = 0; i < 5; i++)
    {
        Serial.print(F("Motor "));
        Serial.print(i);
        Serial.print(F(": "));
        Serial.print(steppers[i].default_steps);
        Serial.println(" steps");

        Serial.print(F("Motor "));
        Serial.print(i);
        Serial.print(F(": "));
        Serial.print(steppers[i].default_delay);
        Serial.println(" delay");

        Serial.print("Motor ");
        Serial.print(i);
        Serial.print(" position: ");
        Serial.println(steppers[i].stepPosition);
    }

    Serial.print(F("Delay inhale (s): "));
    Serial.println(DELAY_INHALE);

    Serial.print(F("Delay exhale (s): "));
    Serial.println(DELAY_EXHALE);

    Serial.print(F("Start maneuver: "));
    Serial.println(START_MANEUVER);
}



void loop() {

    recvWithStartEndMarkers();
    if (newData == true) {
        strcpy(tempChars, receivedChars);
            // this temporary copy is necessary to protect the original data
            //   because strtok() used in parseData() replaces the commas with \0
        checkType();
        newData = false;
        // Serial.print(F("remainingSteppersFlag: "));
        // Serial.println(remainingSteppersFlag, BIN);
    }

}
