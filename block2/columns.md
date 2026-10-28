# What is in each column of `data/gaia_physics1.csv`

All 16 columns come from the Gaia DR3 table `gaiadr3.gaia_source`. Official documentation:
[Gaia DR3 data model — `gaia_source`](https://gea.esac.esa.int/archive/documentation/GDR3/Gaia_archive/chap_datamodel/sec_dm_main_source_catalogue/ssec_dm_gaia_source.html)
(each field has its own entry on that page, in the same order as the table).

**Sources for this table.** Units and the short official description of every column were taken
directly from the Gaia archive's own metadata (`TAP_SCHEMA.columns` for `gaiadr3.gaia_source`,
queried 2026-10-28). The documentation website returned HTTP 503 (unavailable) while this file was
written, so each link points to the `gaia_source` page itself rather than to an anchor inside it,
and the longer explanations below should be checked against that page once it is back up.

`mas` = milliarcsecond = 0.001 arcsecond. `mas/yr` = milliarcseconds per year.

| Column | What it measures (plain words) | Units | Official description (archive metadata) | Documentation |
|---|---|---|---|---|
| `source_id` | A unique ID number for the star. Just a label: it is not a measurement (it does encode the star's rough position on the sky). | none | Unique source identifier (unique within a particular Data Release) | [gaia_source data model](https://gea.esac.esa.int/archive/documentation/GDR3/Gaia_archive/chap_datamodel/sec_dm_main_source_catalogue/ssec_dm_gaia_source.html) |
| `ra` | Right ascension: the star's east–west position on the sky (like longitude), in the equatorial (ICRS) system, at Gaia's reference epoch J2016.0. | deg | Right ascension | [gaia_source data model](https://gea.esac.esa.int/archive/documentation/GDR3/Gaia_archive/chap_datamodel/sec_dm_main_source_catalogue/ssec_dm_gaia_source.html) |
| `dec` | Declination: the star's north–south position on the sky (like latitude), in the same system and epoch as `ra`. | deg | Declination | [gaia_source data model](https://gea.esac.esa.int/archive/documentation/GDR3/Gaia_archive/chap_datamodel/sec_dm_main_source_catalogue/ssec_dm_gaia_source.html) |
| `l` | Galactic longitude: position on the sky measured along the plane of the Milky Way; `l` = 0° points toward the Galactic centre. | deg | Galactic longitude | [gaia_source data model](https://gea.esac.esa.int/archive/documentation/GDR3/Gaia_archive/chap_datamodel/sec_dm_main_source_catalogue/ssec_dm_gaia_source.html) |
| `b` | Galactic latitude: angle above (+) or below (−) the plane of the Milky Way. | deg | Galactic latitude | [gaia_source data model](https://gea.esac.esa.int/archive/documentation/GDR3/Gaia_archive/chap_datamodel/sec_dm_main_source_catalogue/ssec_dm_gaia_source.html) |
| `parallax` | The small back-and-forth shift in the star's apparent position as Earth orbits the Sun. Nearer stars shift more. | mas | Parallax | [gaia_source data model](https://gea.esac.esa.int/archive/documentation/GDR3/Gaia_archive/chap_datamodel/sec_dm_main_source_catalogue/ssec_dm_gaia_source.html) |
| `parallax_error` | The 1-sigma uncertainty on `parallax`. | mas | Standard error of parallax | [gaia_source data model](https://gea.esac.esa.int/archive/documentation/GDR3/Gaia_archive/chap_datamodel/sec_dm_main_source_catalogue/ssec_dm_gaia_source.html) |
| `pmra` | Proper motion in the east–west (right ascension) direction: how fast the star's position drifts across the sky. It is already multiplied by cos(dec), so it is a true angle per year on the sky. | mas/yr | Proper motion in right ascension direction | [gaia_source data model](https://gea.esac.esa.int/archive/documentation/GDR3/Gaia_archive/chap_datamodel/sec_dm_main_source_catalogue/ssec_dm_gaia_source.html) |
| `pmra_error` | The 1-sigma uncertainty on `pmra`. | mas/yr | Standard error of proper motion in right ascension direction | [gaia_source data model](https://gea.esac.esa.int/archive/documentation/GDR3/Gaia_archive/chap_datamodel/sec_dm_main_source_catalogue/ssec_dm_gaia_source.html) |
| `pmdec` | Proper motion in the north–south (declination) direction. | mas/yr | Proper motion in declination direction | [gaia_source data model](https://gea.esac.esa.int/archive/documentation/GDR3/Gaia_archive/chap_datamodel/sec_dm_main_source_catalogue/ssec_dm_gaia_source.html) |
| `pmdec_error` | The 1-sigma uncertainty on `pmdec`. | mas/yr | Standard error of proper motion in declination direction | [gaia_source data model](https://gea.esac.esa.int/archive/documentation/GDR3/Gaia_archive/chap_datamodel/sec_dm_main_source_catalogue/ssec_dm_gaia_source.html) |
| `radial_velocity` | How fast the star moves toward or away from us, measured from the Doppler shift of lines in its spectrum (Gaia's RVS spectrograph). Positive = moving away, negative = approaching. Measured relative to the Solar System barycentre. | km/s | Radial velocity | [gaia_source data model](https://gea.esac.esa.int/archive/documentation/GDR3/Gaia_archive/chap_datamodel/sec_dm_main_source_catalogue/ssec_dm_gaia_source.html) |
| `radial_velocity_error` | The uncertainty on `radial_velocity`. | km/s | Radial velocity error | [gaia_source data model](https://gea.esac.esa.int/archive/documentation/GDR3/Gaia_archive/chap_datamodel/sec_dm_main_source_catalogue/ssec_dm_gaia_source.html) |
| `phot_g_mean_mag` | How bright the star looks in Gaia's broad G band (roughly 330–1050 nm), as an apparent magnitude: **smaller numbers are brighter**. Vega magnitude system. | mag | G-band mean magnitude | [gaia_source data model](https://gea.esac.esa.int/archive/documentation/GDR3/Gaia_archive/chap_datamodel/sec_dm_main_source_catalogue/ssec_dm_gaia_source.html) |
| `bp_rp` | Colour: the blue-band (BP) magnitude minus the red-band (RP) magnitude, i.e. `phot_bp_mean_mag − phot_rp_mean_mag`. Larger values mean a redder (usually cooler) star; smaller values mean bluer (hotter). Empty when BP or RP photometry is missing. | mag | BP - RP colour | [gaia_source data model](https://gea.esac.esa.int/archive/documentation/GDR3/Gaia_archive/chap_datamodel/sec_dm_main_source_catalogue/ssec_dm_gaia_source.html) |
| `ruwe` | Renormalised Unit Weight Error: a quality score for how well Gaia's single-star model (position + parallax + proper motion) fits the measurements. It is the square root of the fit's normalised chi-square, rescaled so that RUWE ≈ 1.0 for a well-behaved source. Values well above 1 mean the star deviates from the simple single-star model, which can be real (e.g. the wobble of an unresolved binary) or spurious (calibration problems). A cut of RUWE < 1.4 is widely used for "good" astrometry. Not given for stars with only a position (2-parameter solution). No units. | none | Renormalised unit weight error | [gaia_source data model](https://gea.esac.esa.int/archive/documentation/GDR3/Gaia_archive/chap_datamodel/sec_dm_main_source_catalogue/ssec_dm_gaia_source.html) |

## How the four motion columns connect to parallax and proper motion (lecture)

| Column | Lecture idea | Direction measured | How you use it |
|---|---|---|---|
| `parallax` | **Parallax**: as Earth moves around the Sun (1 AU baseline), a nearby star appears to move against distant ones. The parallax angle *p* is half of that shift. | It is an angle measured **across the sky**, but what it tells you is distance **along the line of sight**. | distance in parsecs = 1 / *p* in arcseconds, i.e. *d* [pc] = 1000 / `parallax` [mas]. |
| `pmra` | **Proper motion**: the star's steady drift across the sky from its own motion through space (separate from the yearly parallax wobble). | **Across the sky** (east–west component). | Total proper motion μ = √(`pmra`² + `pmdec`²). |
| `pmdec` | **Proper motion**, north–south component. | **Across the sky** (north–south component). | Speed across the sky (tangential velocity) v_t = 4.74 × μ [arcsec/yr] × *d* [pc] km/s = 4.74 × μ [mas/yr] / `parallax` [mas] km/s. |
| `radial_velocity` | The part of the star's velocity that proper motion **cannot** see: motion straight toward or away from us, from the Doppler shift. | **Along our line of sight**. | Combined with v_t it gives the full 3-D speed: v = √(v_t² + v_r²). |

So parallax gives the distance, proper motion (`pmra`, `pmdec`) times distance gives the two velocity
components across the sky, and `radial_velocity` gives the third component along the line of sight.

## Verification (2026-10-28)

The official `gaia_source` documentation page could not be opened: every page under
`gea.esac.esa.int/archive/documentation/GDR3/` returned HTTP 503 (service unavailable), while
the main archive and ESA's Gaia site were up. So the items were checked against other official sources:

| Item | Checked against | Result |
|---|---|---|
| Units of all 16 columns | Gaia archive's own column metadata (`TAP_SCHEMA.columns` for `gaiadr3.gaia_source`), compared line by line | All 16 match |
| `bp_rp` = BP − RP | Downloaded `phot_bp_mean_mag` and `phot_rp_mean_mag` from the archive for 3,746 of our stars and computed BP − RP | Agrees with `bp_rp` to 1.2 × 10⁻⁶ mag (rounding); `bp_rp` is empty exactly when BP or RP is missing |
| `ruwe` description | Lindegren et al. 2021, *Gaia EDR3: The astrometric solution*, A&A 649, A2 ([arXiv:2012.03380](https://arxiv.org/abs/2012.03380)), Sections 5.1 and 5.3 | Confirmed: derived from the normalised chi-square of the fit, RUWE ≈ 1.0 for well-behaved sources, sensitive to unresolved binaries, not given for 2-parameter solutions. Our median RUWE (1.019) agrees with the paper's Table 4. The 1.4 cut is **not** in this paper (it comes from the DR2 RUWE technical note, GAIA-C3-TN-LU-LL-124, which returned HTTP 403). |
| `pmra` includes cos(dec) | Same paper, Section 3.1: "μα∗ = μα cos δ" | Confirmed |
| Reference epoch J2016.0 | [ESA Gaia DR3 page](https://www.cosmos.esa.int/web/gaia/dr3): "The reference epoch for Gaia DR3 ... is 2016.0" | Confirmed |
| Documentation link | ESA Gaia DR3 page lists the official data model at `.../GDR3/Gaia_archive/chap_datamodel/`; our link is the `gaia_source` page inside it | **Not confirmed live** (503). Re-open the link when the documentation site is back up. |
| G band ≈ 330–1050 nm; Vega magnitudes; RV positive = receding, relative to the barycentre | — | **Not verified** against a source in this check (the passband page gives the curves only as a figure) |
