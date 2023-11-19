
// Motor control parameters
// int (*p)[5][500];

// Maneuver arrays
const PROGMEM unsigned int identity[500] = {1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1};

const PROGMEM unsigned int identity_inhale[5][500] = {
  {2965, 1768, 1454, 1284, 1171, 1090, 1028, 978, 937, 902, 872, 846, 823, 803, 784, 768, 753, 740, 727, 716, 705, 696, 687, 678, 670, 663, 656, 650, 644, 638, 633, 628, 623, 618, 614, 610, 606, 602, 599, 595, 592, 589, 586, 583, 581, 578, 576, 574, 571, 569, 567, 565, 563, 562, 560, 558, 557, 555, 554, 553, 551, 550, 549, 548, 547, 546, 544, 544, 543, 542, 541, 540, 539, 538, 538, 537, 536, 535, 535, 534, 534, 533, 532, 532, 531, 531, 530, 529, 529, 528, 528, 527, 527, 526, 526, 525, 525, 524, 524, 523, 523, 522, 522, 522, 521, 521, 520, 520, 520, 520, 520, 520, 520, 520, 520, 521, 521, 521, 522, 523, 524, 524, 525, 526, 528, 529, 530, 532, 533, 535, 536, 538, 540, 542, 544, 546, 548, 550, 552, 555, 557, 559, 562, 565, 567, 570, 573, 576, 578, 581, 584, 588, 591, 594, 597, 601, 604, 608, 611, 615, 619, 623, 626, 630, 635, 639, 643, 647, 652, 656, 661, 665, 670, 675, 680, 685, 690, 695, 701, 706, 712, 717, 723, 729, 735, 741, 747, 754, 760, 767, 774, 781, 788, 796, 803, 811, 819, 827, 835, 844},
  {730, 672, 626, 589, 557, 531, 510, 491, 475, 462, 450, 440, 431, 423, 416, 410, 405, 400, 396, 392, 389, 386, 384, 381, 379, 377, 376, 374, 373, 372, 371, 371, 370, 369, 369, 369, 369, 369, 369, 369, 369, 369, 370, 370, 371, 371, 372, 372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 383, 385, 386, 387, 389, 390, 392, 393, 395, 397, 398, 400, 402, 404, 405, 407, 409, 411, 413, 415, 417, 419, 422, 424, 426, 428, 431, 433, 436, 438, 441, 443, 446, 449, 451, 454, 457, 460, 463, 466, 469, 472, 475, 478, 482, 485, 489, 492, 496, 499, 503, 507, 510, 514, 518, 522, 526, 531, 535, 539, 544, 548, 553, 557, 562, 567, 572, 577, 582, 588, 593, 598, 604, 610, 616, 622, 628, 634, 640, 647, 654, 661, 668, 675, 682, 689, 697, 705, 713, 721, 730, 738, 747, 756, 766, 775, 785, 795, 806, 816, 827, 838, 850, 862, 874, 887, 900, 913, 927, 942, 956, 972, 987, 1004, 1020, 1038, 1056, 1075, 1094, 1114, 1135, 1157, 1179, 1203, 1227, 1252, 1279, 1307, 1336, 1366, 1398, 1431, 1466, 1502, 1541, 1582, 1624, 1670, 1717, 1768, 1822, 1879},
  {612, 610, 608, 607, 605, 603, 601, 600, 598, 596, 595, 593, 591, 590, 588, 586, 585, 583, 582, 580, 578, 577, 575, 574, 572, 570, 569, 567, 566, 564, 563, 561, 560, 558, 557, 555, 554, 552, 551, 550, 548, 547, 545, 544, 543, 541, 540, 538, 537, 536, 534, 533, 532, 530, 529, 528, 526, 525, 524, 522, 521, 520, 518, 517, 516, 515, 513, 512, 511, 510, 508, 507, 506, 505, 504, 502, 501, 500, 499, 498, 496, 495, 494, 493, 492, 491, 489, 488, 487, 486, 485, 484, 483, 482, 481, 479, 478, 477, 476, 475, 474, 473, 472, 471, 470, 469, 468, 467, 466, 465, 464, 463, 462, 461, 459, 458, 457, 457, 456, 455, 454, 453, 452, 451, 450, 449, 448, 447, 446, 445, 444, 443, 442, 441, 440, 439, 438, 437, 437, 436, 435, 434, 433, 432, 431, 430, 429, 429, 428, 427, 426, 425, 424, 423, 423, 422, 421, 420, 419, 418, 418, 417, 416, 415, 414, 413, 413, 412, 411, 410, 409, 409, 408, 407, 406, 405, 405, 404, 403, 402, 402, 401, 400, 399, 398, 398, 397, 396, 395, 395, 394, 393, 393, 392, 391, 390, 390, 389, 388, 387},
  {501, 500, 499, 498, 497, 495, 494, 493, 492, 491, 490, 489, 488, 486, 485, 484, 483, 482, 481, 480, 479, 478, 477, 476, 475, 474, 473, 472, 470, 469, 468, 467, 466, 465, 464, 463, 462, 461, 460, 459, 458, 457, 456, 455, 455, 454, 453, 452, 451, 450, 449, 448, 447, 446, 445, 444, 443, 442, 441, 441, 440, 439, 438, 437, 436, 435, 434, 433, 433, 432, 431, 430, 429, 428, 427, 427, 426, 425, 424, 423, 422, 421, 421, 420, 419, 418, 417, 417, 416, 415, 414, 413, 413, 412, 411, 410, 409, 409, 408, 407, 406, 406, 405, 404, 403, 403, 402, 401, 400, 400, 399, 398, 397, 397, 396, 395, 394, 394, 393, 392, 391, 391, 390, 389, 389, 388, 387, 387, 386, 385, 384, 384, 383, 382, 382, 381, 380, 380, 379, 378, 378, 377, 376, 376, 375, 374, 374, 373, 372, 372, 371, 371, 370, 369, 369, 368, 367, 367, 366, 365, 365, 364, 364, 363, 362, 362, 361, 361, 360, 359, 359, 358, 358, 357, 356, 356, 355, 355, 354, 353, 353, 352, 352, 351, 351, 350, 349, 349, 348, 348, 347, 347, 346, 345, 345, 344, 344, 343, 343, 342},
  {635, 633, 631, 628, 626, 624, 622, 620, 618, 616, 614, 612, 610, 608, 606, 605, 603, 601, 599, 597, 595, 593, 591, 590, 588, 586, 584, 582, 581, 579, 577, 575, 574, 572, 570, 568, 567, 565, 563, 562, 560, 558, 557, 555, 554, 552, 550, 549, 547, 546, 544, 543, 541, 540, 538, 536, 535, 533, 532, 531, 529, 528, 526, 525, 523, 522, 520, 519, 518, 516, 515, 513, 512, 511, 509, 508, 507, 505, 504, 503, 501, 500, 499, 497, 496, 495, 493, 492, 491, 490, 488, 487, 486, 485, 483, 482, 481, 480, 479, 477, 476, 475, 474, 473, 471, 470, 469, 468, 467, 466, 465, 463, 462, 461, 460, 459, 458, 457, 456, 455, 453, 452, 451, 450, 449, 448, 447, 446, 445, 444, 443, 442, 441, 440, 439, 438, 437, 436, 435, 434, 433, 432, 431, 430, 429, 428, 427, 426, 425, 424, 423, 422, 421, 420, 420, 419, 418, 417, 416, 415, 414, 413, 412, 411, 410, 410, 409, 408, 407, 406, 405, 404, 404, 403, 402, 401, 400, 399, 398, 398, 397, 396, 395, 394, 394, 393, 392, 391, 390, 390, 389, 388, 387, 386, 386, 385, 384, 383, 382, 382}
  };

const PROGMEM unsigned int identity_exhale[5][500] = {
  {3000, 3000, 2997, 2887, 2784, 2689, 2601, 2518, 2441, 2368, 2300, 2236, 2176, 2118, 2064, 2013, 1965, 1918, 1875, 1833, 1793, 1755, 1719, 1684, 1650, 1619, 1588, 1559, 1531, 1503, 1477, 1452, 1428, 1405, 1382, 1361, 1340, 1320, 1300, 1281, 1263, 1245, 1228, 1211, 1195, 1179, 1164, 1150, 1135, 1121, 1108, 1095, 1082, 1069, 1057, 1046, 1034, 1023, 1012, 1001, 991, 981, 971, 962, 952, 943, 934, 925, 917, 909, 900, 892, 885, 877, 870, 862, 855, 848, 842, 835, 828, 822, 816, 810, 804, 798, 792, 786, 781, 775, 770, 765, 760, 755, 750, 745, 740, 736, 731, 727, 722, 718, 714, 710, 706, 702, 698, 694, 690, 686, 683, 679, 676, 672, 669, 666, 662, 659, 656, 653, 650, 647, 644, 641, 639, 636, 633, 631, 628, 625, 623, 621, 618, 616, 613, 611, 609, 607, 605, 603, 601, 599, 597, 595, 593, 591, 589, 587, 586, 584, 582, 581, 579, 578, 576, 575, 573, 572, 570, 569, 568, 567, 565, 564, 563, 562, 561, 560, 559, 558, 557, 556, 555, 554, 553, 553, 552, 551, 550, 550, 549, 549, 548, 547, 547, 546, 546, 546, 545, 545, 545, 544, 544, 544, 543, 543, 543, 543, 543, 543},
  {350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365, 366, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 380, 381, 382, 383, 384, 385, 387, 388, 389, 390, 391, 392, 394, 395, 396, 397, 399, 400, 401, 402, 404, 405, 406, 408, 409, 410, 411, 413, 414, 416, 417, 418, 420, 421, 422, 424, 425, 427, 428, 430, 431, 432, 434, 435, 437, 438, 440, 441, 443, 444, 446, 448, 449, 451, 452, 454, 456, 457, 459, 461, 462, 464, 466, 467, 469, 471, 473, 474, 476, 478, 480, 481, 483, 485, 487, 489, 491, 493, 495, 496, 498, 500, 502, 504, 506, 508, 510, 512, 514, 517, 519, 521, 523, 525, 527, 529, 532, 534, 536, 538, 541, 543, 545, 548, 550, 552, 555, 557, 560, 562, 565, 567, 570, 572, 575, 577, 580, 583, 585, 588, 591, 594, 596, 599, 602, 605, 608, 611, 614, 617, 620, 623, 626, 629, 632, 635, 638, 641, 645, 648, 651, 655, 658, 661, 665, 668, 672, 675, 679, 683, 686, 690, 694, 697, 701, 705, 709, 713, 717, 721, 725, 729, 734, 738, 742, 746, 751, 755, 760, 764, 769, 774},
  {350, 351, 352, 352, 353, 353, 354, 355, 355, 356, 356, 357, 358, 358, 359, 360, 360, 361, 362, 362, 363, 363, 364, 365, 365, 366, 367, 367, 368, 369, 369, 370, 371, 371, 372, 373, 373, 374, 375, 376, 376, 377, 378, 378, 379, 380, 380, 381, 382, 383, 383, 384, 385, 385, 386, 387, 388, 388, 389, 390, 391, 391, 392, 393, 394, 394, 395, 396, 397, 398, 398, 399, 400, 401, 401, 402, 403, 404, 405, 405, 406, 407, 408, 409, 409, 410, 411, 412, 413, 414, 414, 415, 416, 417, 418, 419, 420, 420, 421, 422, 423, 424, 425, 426, 427, 428, 428, 429, 430, 431, 432, 433, 434, 435, 436, 437, 438, 439, 440, 440, 441, 442, 443, 444, 445, 446, 447, 448, 449, 450, 451, 452, 453, 454, 455, 456, 457, 458, 459, 460, 461, 462, 463, 465, 466, 467, 468, 469, 470, 471, 472, 473, 474, 475, 476, 478, 479, 480, 481, 482, 483, 484, 486, 487, 488, 489, 490, 491, 493, 494, 495, 496, 497, 499, 500, 501, 502, 504, 505, 506, 507, 509, 510, 511, 512, 514, 515, 516, 518, 519, 520, 522, 523, 524, 526, 527, 528, 530, 531, 532},
  {342, 343, 344, 345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365, 367, 368, 369, 370, 371, 372, 373, 374, 375, 377, 378, 379, 380, 381, 382, 384, 385, 386, 387, 388, 390, 391, 392, 393, 395, 396, 397, 398, 400, 401, 402, 404, 405, 406, 408, 409, 410, 412, 413, 415, 416, 417, 419, 420, 422, 423, 424, 426, 427, 429, 430, 432, 433, 435, 436, 438, 440, 441, 443, 444, 446, 448, 449, 451, 452, 454, 456, 457, 459, 461, 463, 464, 466, 468, 470, 471, 473, 475, 477, 479, 481, 482, 484, 486, 488, 490, 492, 494, 496, 498, 500, 502, 504, 506, 508, 510, 513, 515, 517, 519, 521, 523, 526, 528, 530, 532, 535, 537, 539, 542, 544, 547, 549, 551, 554, 556, 559, 561, 564, 567, 569, 572, 574, 577, 580, 583, 585, 588, 591, 594, 597, 600, 602, 605, 608, 611, 614, 617, 621, 624, 627, 630, 633, 637, 640, 643, 647, 650, 653, 657, 660, 664, 668, 671, 675, 678, 682, 686, 690, 694, 698, 702, 706, 710, 714, 718, 722, 726, 731, 735, 739, 744, 748, 753, 757, 762},
  {371, 372, 373, 374, 375, 376, 378, 379, 380, 381, 382, 384, 385, 386, 387, 388, 390, 391, 392, 393, 395, 396, 397, 399, 400, 401, 403, 404, 405, 407, 408, 409, 411, 412, 414, 415, 416, 418, 419, 421, 422, 424, 425, 427, 428, 430, 431, 433, 434, 436, 437, 439, 441, 442, 444, 446, 447, 449, 450, 452, 454, 456, 457, 459, 461, 462, 464, 466, 468, 470, 471, 473, 475, 477, 479, 481, 483, 485, 487, 489, 491, 493, 495, 497, 499, 501, 503, 505, 507, 509, 511, 513, 516, 518, 520, 522, 524, 527, 529, 531, 534, 536, 538, 541, 543, 546, 548, 551, 553, 556, 558, 561, 563, 566, 569, 571, 574, 577, 580, 582, 585, 588, 591, 594, 597, 600, 603, 606, 609, 612, 615, 618, 621, 624, 627, 631, 634, 637, 641, 644, 648, 651, 655, 658, 662, 665, 669, 673, 676, 680, 684, 688, 692, 696, 700, 704, 708, 712, 716, 721, 725, 729, 734, 738, 743, 747, 752, 756, 761, 766, 771, 776, 781, 786, 791, 796, 801, 807, 812, 818, 823, 829, 834, 840, 846, 852, 858, 864, 870, 877, 883, 889, 896, 903, 909, 916, 923, 930, 937, 945}
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
  // p = steps > 0 ? &inhale_delays : &exhale_delays;
  // TODO: update delay values for inhale or exhale. Retrieve from progmem or lobe default
  unsigned int displayInt;
  if (si.dir == inhale) {
    for (int k = 0; k < 500; k++) {
    displayInt = pgm_read_word_near(&(identity_inhale[whichMotor][k]));
    delays[whichMotor][k] = displayInt;
    Serial.print(displayInt);
    Serial.print(',');
  }
  } else {
    for (int k = 0; k < 500; k++) {
    displayInt = pgm_read_word_near(&(identity_exhale[whichMotor][k]));
    delays[whichMotor][k] = displayInt;
    Serial.print(displayInt);
    Serial.print(',');
  }
  }
  Serial.println();
  
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
        if (strcmp(tempChars, "PROFILE") == 0)
        {
            run_profile_constant();
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

void prepareM(int i, int steps) {
    Serial.print(i);
    Serial.print(F(": "));
    Serial.print(steps);
    Serial.println(" steps");
    prepareMovement(i, steps);
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

void run_profile_constant() {
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

void printInvalid() {
    Serial.println(F("Invalid command"));
}

void printDelays() {
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
