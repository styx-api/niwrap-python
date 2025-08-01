# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRI_VOLSYNTH_METADATA = Metadata(
    id="ac2fbdf3f2279fbed0fc7c55ea50f3f4eb111eb3.boutiques",
    name="mri_volsynth",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


MriVolsynthParameters = typing.TypedDict('MriVolsynthParameters', {
    "__STYXTYPE__": typing.Literal["mri_volsynth"],
    "output_volid": str,
    "template": typing.NotRequired[str | None],
    "nframes": typing.NotRequired[float | None],
    "offset_flag": bool,
    "offset_mid_flag": bool,
    "curv": typing.NotRequired[str | None],
    "dim": typing.NotRequired[list[float] | None],
    "res": typing.NotRequired[list[float] | None],
    "vox_size": typing.NotRequired[list[float] | None],
    "tr": typing.NotRequired[float | None],
    "cdircos": typing.NotRequired[list[float] | None],
    "rdircos": typing.NotRequired[list[float] | None],
    "sdircos": typing.NotRequired[list[float] | None],
    "c_ras": typing.NotRequired[list[float] | None],
    "p0": typing.NotRequired[list[float] | None],
    "precision": typing.NotRequired[str | None],
    "seed": typing.NotRequired[float | None],
    "seedfile": typing.NotRequired[InputPathType | None],
    "pdf": typing.NotRequired[str | None],
    "bb": typing.NotRequired[list[float] | None],
    "gmean": typing.NotRequired[float | None],
    "gstd": typing.NotRequired[float | None],
    "delta_crsf": typing.NotRequired[list[float] | None],
    "delta_val": typing.NotRequired[float | None],
    "delta_val_off": typing.NotRequired[float | None],
    "grid": typing.NotRequired[list[float] | None],
    "dof": typing.NotRequired[float | None],
    "dof_num": typing.NotRequired[float | None],
    "dof_den": typing.NotRequired[float | None],
    "rescale_flag": bool,
    "val_a": typing.NotRequired[float | None],
    "val_b": typing.NotRequired[float | None],
    "vox_radius": typing.NotRequired[float | None],
    "mm_radius": typing.NotRequired[float | None],
    "sphere_center": typing.NotRequired[list[float] | None],
    "hsc": typing.NotRequired[list[float] | None],
    "abs_flag": bool,
    "cp": typing.NotRequired[InputPathType | None],
    "spike": typing.NotRequired[float | None],
    "fwhm": typing.NotRequired[float | None],
    "sum2": typing.NotRequired[InputPathType | None],
    "dim_surf_flag": bool,
    "ctab": typing.NotRequired[InputPathType | None],
})


def dyn_cargs(
    t: str,
) -> typing.Any:
    """
    Get build cargs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build cargs function.
    """
    return {
        "mri_volsynth": mri_volsynth_cargs,
    }.get(t)


def dyn_outputs(
    t: str,
) -> typing.Any:
    """
    Get build outputs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build outputs function.
    """
    return {
    }.get(t)


class MriVolsynthOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_volsynth(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def mri_volsynth_params(
    output_volid: str,
    template: str | None = None,
    nframes: float | None = None,
    offset_flag: bool = False,
    offset_mid_flag: bool = False,
    curv: str | None = None,
    dim: list[float] | None = None,
    res: list[float] | None = None,
    vox_size: list[float] | None = None,
    tr: float | None = None,
    cdircos: list[float] | None = None,
    rdircos: list[float] | None = None,
    sdircos: list[float] | None = None,
    c_ras: list[float] | None = None,
    p0: list[float] | None = None,
    precision: str | None = None,
    seed: float | None = None,
    seedfile: InputPathType | None = None,
    pdf: str | None = None,
    bb: list[float] | None = None,
    gmean: float | None = None,
    gstd: float | None = None,
    delta_crsf: list[float] | None = None,
    delta_val: float | None = None,
    delta_val_off: float | None = None,
    grid: list[float] | None = None,
    dof: float | None = None,
    dof_num: float | None = None,
    dof_den: float | None = None,
    rescale_flag: bool = False,
    val_a: float | None = None,
    val_b: float | None = None,
    vox_radius: float | None = None,
    mm_radius: float | None = None,
    sphere_center: list[float] | None = None,
    hsc: list[float] | None = None,
    abs_flag: bool = False,
    cp: InputPathType | None = None,
    spike: float | None = None,
    fwhm: float | None = None,
    sum2: InputPathType | None = None,
    dim_surf_flag: bool = False,
    ctab: InputPathType | None = None,
) -> MriVolsynthParameters:
    """
    Build parameters.
    
    Args:
        output_volid: Output volume path id and format.
        template: Template volume id.
        nframes: Override template number of frames.
        offset_flag: Use template as intensity offset.
        offset_mid_flag: Use middle frame of template as intensity offset.
        curv: Save output as curvature, uses lh.thickness as template. Requires\
            subject and hemisphere.
        dim: Specify dimensionality nc nr ns nf.
        res: Voxel resolution dc dr ds df (df is TR, in msec).
        vox_size: Change template voxel resolution and dimension dc dr ds.
        tr: Time between frames in msec.
        cdircos: Column cosine direction x, y, z.
        rdircos: Row cosine direction x, y, z.
        sdircos: Slice cosine direction x, y, z.
        c_ras: RAS coordinates of 'center' voxel c_r c_a c_s.
        p0: First voxel coordinates p0r p0a p0s.
        precision: Precision of the output (e.g., float).
        seed: Seed for the random number generator.
        seedfile: Write seed value to this file.
        pdf: Probability distribution function (e.g., gaussian, uniform, const).
        bb: Bounding box c r s dc dr ds (In=ValA, Out=ValB).
        gmean: Mean for the gaussian distribution.
        gstd: Standard deviation for the gaussian distribution.
        delta_crsf: Delta's col, row, slice, and frame coordinates.
        delta_val: Delta value.
        delta_val_off: Delta background value.
        grid: Grid dimensions dcol, drow, dslice.
        dof: Degrees of freedom for t and chi2 distributions.
        dof_num: Numerator degrees of freedom for F distribution.
        dof_den: Denominator degrees of freedom for F distribution.
        rescale_flag: Rescale z, t, F, or chi2 after smoothing.
        val_a: Set ValA.
        val_b: Set ValB.
        vox_radius: Radius in voxels for sphere.
        mm_radius: Radius in mm for sphere.
        sphere_center: Sphere center coordinates column, row, slice.
        hsc: Multiply each frame by a random number between min and max.
        abs_flag: Compute absolute value.
        cp: Set control point voxels to 1.
        spike: Set all values at a given time point to 1e9.
        fwhm: Smooth by Full Width at Half Maximum (FWHM) in mm.
        sum2: Save sum of volume squared into specified file.
        dim_surf_flag: Set dimension to nvertices x 1 x 1.
        ctab: Embed color table.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mri_volsynth",
        "output_volid": output_volid,
        "offset_flag": offset_flag,
        "offset_mid_flag": offset_mid_flag,
        "rescale_flag": rescale_flag,
        "abs_flag": abs_flag,
        "dim_surf_flag": dim_surf_flag,
    }
    if template is not None:
        params["template"] = template
    if nframes is not None:
        params["nframes"] = nframes
    if curv is not None:
        params["curv"] = curv
    if dim is not None:
        params["dim"] = dim
    if res is not None:
        params["res"] = res
    if vox_size is not None:
        params["vox_size"] = vox_size
    if tr is not None:
        params["tr"] = tr
    if cdircos is not None:
        params["cdircos"] = cdircos
    if rdircos is not None:
        params["rdircos"] = rdircos
    if sdircos is not None:
        params["sdircos"] = sdircos
    if c_ras is not None:
        params["c_ras"] = c_ras
    if p0 is not None:
        params["p0"] = p0
    if precision is not None:
        params["precision"] = precision
    if seed is not None:
        params["seed"] = seed
    if seedfile is not None:
        params["seedfile"] = seedfile
    if pdf is not None:
        params["pdf"] = pdf
    if bb is not None:
        params["bb"] = bb
    if gmean is not None:
        params["gmean"] = gmean
    if gstd is not None:
        params["gstd"] = gstd
    if delta_crsf is not None:
        params["delta_crsf"] = delta_crsf
    if delta_val is not None:
        params["delta_val"] = delta_val
    if delta_val_off is not None:
        params["delta_val_off"] = delta_val_off
    if grid is not None:
        params["grid"] = grid
    if dof is not None:
        params["dof"] = dof
    if dof_num is not None:
        params["dof_num"] = dof_num
    if dof_den is not None:
        params["dof_den"] = dof_den
    if val_a is not None:
        params["val_a"] = val_a
    if val_b is not None:
        params["val_b"] = val_b
    if vox_radius is not None:
        params["vox_radius"] = vox_radius
    if mm_radius is not None:
        params["mm_radius"] = mm_radius
    if sphere_center is not None:
        params["sphere_center"] = sphere_center
    if hsc is not None:
        params["hsc"] = hsc
    if cp is not None:
        params["cp"] = cp
    if spike is not None:
        params["spike"] = spike
    if fwhm is not None:
        params["fwhm"] = fwhm
    if sum2 is not None:
        params["sum2"] = sum2
    if ctab is not None:
        params["ctab"] = ctab
    return params


def mri_volsynth_cargs(
    params: MriVolsynthParameters,
    execution: Execution,
) -> list[str]:
    """
    Build command-line arguments from parameters.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Command-line arguments.
    """
    cargs = []
    cargs.append("mri_volsynth")
    cargs.extend([
        "--o",
        params.get("output_volid")
    ])
    if params.get("template") is not None:
        cargs.extend([
            "--template",
            params.get("template")
        ])
    if params.get("nframes") is not None:
        cargs.extend([
            "--nframes",
            str(params.get("nframes"))
        ])
    if params.get("offset_flag"):
        cargs.append("--offset")
    if params.get("offset_mid_flag"):
        cargs.append("--offset-mid")
    if params.get("curv") is not None:
        cargs.extend([
            "--curv",
            params.get("curv")
        ])
    if params.get("dim") is not None:
        cargs.extend([
            "--dim",
            *map(str, params.get("dim"))
        ])
    if params.get("res") is not None:
        cargs.extend([
            "--res",
            *map(str, params.get("res"))
        ])
    if params.get("vox_size") is not None:
        cargs.extend([
            "--vox-size",
            *map(str, params.get("vox_size"))
        ])
    if params.get("tr") is not None:
        cargs.extend([
            "--tr",
            str(params.get("tr"))
        ])
    if params.get("cdircos") is not None:
        cargs.extend([
            "--cdircos",
            *map(str, params.get("cdircos"))
        ])
    if params.get("rdircos") is not None:
        cargs.extend([
            "--rdircos",
            *map(str, params.get("rdircos"))
        ])
    if params.get("sdircos") is not None:
        cargs.extend([
            "--sdircos",
            *map(str, params.get("sdircos"))
        ])
    if params.get("c_ras") is not None:
        cargs.extend([
            "--c_ras",
            *map(str, params.get("c_ras"))
        ])
    if params.get("p0") is not None:
        cargs.extend([
            "--p0",
            *map(str, params.get("p0"))
        ])
    if params.get("precision") is not None:
        cargs.extend([
            "--precision",
            params.get("precision")
        ])
    if params.get("seed") is not None:
        cargs.extend([
            "--seed",
            str(params.get("seed"))
        ])
    if params.get("seedfile") is not None:
        cargs.extend([
            "--seedfile",
            execution.input_file(params.get("seedfile"))
        ])
    if params.get("pdf") is not None:
        cargs.extend([
            "--pdf",
            params.get("pdf")
        ])
    if params.get("bb") is not None:
        cargs.extend([
            "--bb",
            *map(str, params.get("bb"))
        ])
    if params.get("gmean") is not None:
        cargs.extend([
            "--gmean",
            str(params.get("gmean"))
        ])
    if params.get("gstd") is not None:
        cargs.extend([
            "--gstd",
            str(params.get("gstd"))
        ])
    if params.get("delta_crsf") is not None:
        cargs.extend([
            "--delta-crsf",
            *map(str, params.get("delta_crsf"))
        ])
    if params.get("delta_val") is not None:
        cargs.extend([
            "--delta-val",
            str(params.get("delta_val"))
        ])
    if params.get("delta_val_off") is not None:
        cargs.extend([
            "--delta-val-off",
            str(params.get("delta_val_off"))
        ])
    if params.get("grid") is not None:
        cargs.extend([
            "--grid",
            *map(str, params.get("grid"))
        ])
    if params.get("dof") is not None:
        cargs.extend([
            "--dof",
            str(params.get("dof"))
        ])
    if params.get("dof_num") is not None:
        cargs.extend([
            "--dof-num",
            str(params.get("dof_num"))
        ])
    if params.get("dof_den") is not None:
        cargs.extend([
            "--dof-den",
            str(params.get("dof_den"))
        ])
    if params.get("rescale_flag"):
        cargs.append("--rescale")
    if params.get("val_a") is not None:
        cargs.extend([
            "--val-a",
            str(params.get("val_a"))
        ])
    if params.get("val_b") is not None:
        cargs.extend([
            "--val-b",
            str(params.get("val_b"))
        ])
    if params.get("vox_radius") is not None:
        cargs.extend([
            "--vox-radius",
            str(params.get("vox_radius"))
        ])
    if params.get("mm_radius") is not None:
        cargs.extend([
            "--mm-radius",
            str(params.get("mm_radius"))
        ])
    if params.get("sphere_center") is not None:
        cargs.extend([
            "--sphere-center",
            *map(str, params.get("sphere_center"))
        ])
    if params.get("hsc") is not None:
        cargs.extend([
            "--hsc",
            *map(str, params.get("hsc"))
        ])
    if params.get("abs_flag"):
        cargs.append("--abs")
    if params.get("cp") is not None:
        cargs.extend([
            "--cp",
            execution.input_file(params.get("cp"))
        ])
    if params.get("spike") is not None:
        cargs.extend([
            "--spike",
            str(params.get("spike"))
        ])
    if params.get("fwhm") is not None:
        cargs.extend([
            "--fwhm",
            str(params.get("fwhm"))
        ])
    if params.get("sum2") is not None:
        cargs.extend([
            "--sum2",
            execution.input_file(params.get("sum2"))
        ])
    if params.get("dim_surf_flag"):
        cargs.append("--dim-surf")
    if params.get("ctab") is not None:
        cargs.extend([
            "--ctab",
            execution.input_file(params.get("ctab"))
        ])
    return cargs


def mri_volsynth_outputs(
    params: MriVolsynthParameters,
    execution: Execution,
) -> MriVolsynthOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MriVolsynthOutputs(
        root=execution.output_file("."),
    )
    return ret


def mri_volsynth_execute(
    params: MriVolsynthParameters,
    execution: Execution,
) -> MriVolsynthOutputs:
    """
    Synthesizes a volume with specified geometry and probability distribution
    function.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MriVolsynthOutputs`).
    """
    params = execution.params(params)
    cargs = mri_volsynth_cargs(params, execution)
    ret = mri_volsynth_outputs(params, execution)
    execution.run(cargs)
    return ret


def mri_volsynth(
    output_volid: str,
    template: str | None = None,
    nframes: float | None = None,
    offset_flag: bool = False,
    offset_mid_flag: bool = False,
    curv: str | None = None,
    dim: list[float] | None = None,
    res: list[float] | None = None,
    vox_size: list[float] | None = None,
    tr: float | None = None,
    cdircos: list[float] | None = None,
    rdircos: list[float] | None = None,
    sdircos: list[float] | None = None,
    c_ras: list[float] | None = None,
    p0: list[float] | None = None,
    precision: str | None = None,
    seed: float | None = None,
    seedfile: InputPathType | None = None,
    pdf: str | None = None,
    bb: list[float] | None = None,
    gmean: float | None = None,
    gstd: float | None = None,
    delta_crsf: list[float] | None = None,
    delta_val: float | None = None,
    delta_val_off: float | None = None,
    grid: list[float] | None = None,
    dof: float | None = None,
    dof_num: float | None = None,
    dof_den: float | None = None,
    rescale_flag: bool = False,
    val_a: float | None = None,
    val_b: float | None = None,
    vox_radius: float | None = None,
    mm_radius: float | None = None,
    sphere_center: list[float] | None = None,
    hsc: list[float] | None = None,
    abs_flag: bool = False,
    cp: InputPathType | None = None,
    spike: float | None = None,
    fwhm: float | None = None,
    sum2: InputPathType | None = None,
    dim_surf_flag: bool = False,
    ctab: InputPathType | None = None,
    runner: Runner | None = None,
) -> MriVolsynthOutputs:
    """
    Synthesizes a volume with specified geometry and probability distribution
    function.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        output_volid: Output volume path id and format.
        template: Template volume id.
        nframes: Override template number of frames.
        offset_flag: Use template as intensity offset.
        offset_mid_flag: Use middle frame of template as intensity offset.
        curv: Save output as curvature, uses lh.thickness as template. Requires\
            subject and hemisphere.
        dim: Specify dimensionality nc nr ns nf.
        res: Voxel resolution dc dr ds df (df is TR, in msec).
        vox_size: Change template voxel resolution and dimension dc dr ds.
        tr: Time between frames in msec.
        cdircos: Column cosine direction x, y, z.
        rdircos: Row cosine direction x, y, z.
        sdircos: Slice cosine direction x, y, z.
        c_ras: RAS coordinates of 'center' voxel c_r c_a c_s.
        p0: First voxel coordinates p0r p0a p0s.
        precision: Precision of the output (e.g., float).
        seed: Seed for the random number generator.
        seedfile: Write seed value to this file.
        pdf: Probability distribution function (e.g., gaussian, uniform, const).
        bb: Bounding box c r s dc dr ds (In=ValA, Out=ValB).
        gmean: Mean for the gaussian distribution.
        gstd: Standard deviation for the gaussian distribution.
        delta_crsf: Delta's col, row, slice, and frame coordinates.
        delta_val: Delta value.
        delta_val_off: Delta background value.
        grid: Grid dimensions dcol, drow, dslice.
        dof: Degrees of freedom for t and chi2 distributions.
        dof_num: Numerator degrees of freedom for F distribution.
        dof_den: Denominator degrees of freedom for F distribution.
        rescale_flag: Rescale z, t, F, or chi2 after smoothing.
        val_a: Set ValA.
        val_b: Set ValB.
        vox_radius: Radius in voxels for sphere.
        mm_radius: Radius in mm for sphere.
        sphere_center: Sphere center coordinates column, row, slice.
        hsc: Multiply each frame by a random number between min and max.
        abs_flag: Compute absolute value.
        cp: Set control point voxels to 1.
        spike: Set all values at a given time point to 1e9.
        fwhm: Smooth by Full Width at Half Maximum (FWHM) in mm.
        sum2: Save sum of volume squared into specified file.
        dim_surf_flag: Set dimension to nvertices x 1 x 1.
        ctab: Embed color table.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriVolsynthOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_VOLSYNTH_METADATA)
    params = mri_volsynth_params(
        output_volid=output_volid,
        template=template,
        nframes=nframes,
        offset_flag=offset_flag,
        offset_mid_flag=offset_mid_flag,
        curv=curv,
        dim=dim,
        res=res,
        vox_size=vox_size,
        tr=tr,
        cdircos=cdircos,
        rdircos=rdircos,
        sdircos=sdircos,
        c_ras=c_ras,
        p0=p0,
        precision=precision,
        seed=seed,
        seedfile=seedfile,
        pdf=pdf,
        bb=bb,
        gmean=gmean,
        gstd=gstd,
        delta_crsf=delta_crsf,
        delta_val=delta_val,
        delta_val_off=delta_val_off,
        grid=grid,
        dof=dof,
        dof_num=dof_num,
        dof_den=dof_den,
        rescale_flag=rescale_flag,
        val_a=val_a,
        val_b=val_b,
        vox_radius=vox_radius,
        mm_radius=mm_radius,
        sphere_center=sphere_center,
        hsc=hsc,
        abs_flag=abs_flag,
        cp=cp,
        spike=spike,
        fwhm=fwhm,
        sum2=sum2,
        dim_surf_flag=dim_surf_flag,
        ctab=ctab,
    )
    return mri_volsynth_execute(params, execution)


__all__ = [
    "MRI_VOLSYNTH_METADATA",
    "MriVolsynthOutputs",
    "MriVolsynthParameters",
    "mri_volsynth",
    "mri_volsynth_params",
]
