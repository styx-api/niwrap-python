# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRI_EM_REGISTER_METADATA = Metadata(
    id="8836c49a04dd6a9dcc02bd9442c70610816e97b7.boutiques",
    name="mri_em_register",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


MriEmRegisterParameters = typing.TypedDict('MriEmRegisterParameters', {
    "__STYXTYPE__": typing.Literal["mri_em_register"],
    "input_volume": InputPathType,
    "template_gca": InputPathType,
    "output_transform": str,
    "distance": typing.NotRequired[float | None],
    "nomap": bool,
    "flash": bool,
    "mask": typing.NotRequired[InputPathType | None],
    "skull": bool,
    "uns": typing.NotRequired[float | None],
    "diag": typing.NotRequired[str | None],
    "debug_voxel": typing.NotRequired[list[float] | None],
    "debug_label": typing.NotRequired[float | None],
    "tr": typing.NotRequired[float | None],
    "te": typing.NotRequired[float | None],
    "alpha": typing.NotRequired[float | None],
    "example": typing.NotRequired[list[InputPathType] | None],
    "samples": typing.NotRequired[str | None],
    "fsamples": typing.NotRequired[str | None],
    "nsamples": typing.NotRequired[str | None],
    "contrast": bool,
    "flash_parms": typing.NotRequired[InputPathType | None],
    "transonly": bool,
    "write_mean": typing.NotRequired[str | None],
    "prior": typing.NotRequired[float | None],
    "spacing": typing.NotRequired[float | None],
    "scales": typing.NotRequired[float | None],
    "novar": bool,
    "dt": typing.NotRequired[float | None],
    "tol": typing.NotRequired[float | None],
    "center": bool,
    "noscale": bool,
    "noiscale": bool,
    "num_transforms": typing.NotRequired[float | None],
    "area": typing.NotRequired[float | None],
    "nlarea": typing.NotRequired[float | None],
    "levels": typing.NotRequired[float | None],
    "intensity": typing.NotRequired[float | None],
    "reduce": typing.NotRequired[float | None],
    "n_samples": typing.NotRequired[float | None],
    "norm": typing.NotRequired[str | None],
    "trans": typing.NotRequired[float | None],
    "steps": typing.NotRequired[float | None],
    "long_reg": typing.NotRequired[str | None],
    "cpfile": typing.NotRequired[InputPathType | None],
    "translation_vector": typing.NotRequired[list[float] | None],
    "rotation_vector": typing.NotRequired[list[float] | None],
    "xform": typing.NotRequired[str | None],
    "blur": typing.NotRequired[float | None],
    "diagno": bool,
    "s": typing.NotRequired[float | None],
    "max_angle": typing.NotRequired[float | None],
    "niters": typing.NotRequired[float | None],
    "write_iters": typing.NotRequired[float | None],
    "ctl_point_pct": typing.NotRequired[float | None],
    "momentum": typing.NotRequired[float | None],
    "threads": typing.NotRequired[float | None],
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
        "mri_em_register": mri_em_register_cargs,
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
        "mri_em_register": mri_em_register_outputs,
    }.get(t)


class MriEmRegisterOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_em_register(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_transform_file: OutputPathType
    """Transform in LTA format"""


def mri_em_register_params(
    input_volume: InputPathType,
    template_gca: InputPathType,
    output_transform: str,
    distance: float | None = None,
    nomap: bool = False,
    flash: bool = False,
    mask: InputPathType | None = None,
    skull: bool = False,
    uns: float | None = None,
    diag: str | None = None,
    debug_voxel: list[float] | None = None,
    debug_label: float | None = None,
    tr: float | None = None,
    te: float | None = None,
    alpha: float | None = None,
    example: list[InputPathType] | None = None,
    samples: str | None = None,
    fsamples: str | None = None,
    nsamples: str | None = None,
    contrast: bool = False,
    flash_parms: InputPathType | None = None,
    transonly: bool = False,
    write_mean: str | None = None,
    prior: float | None = None,
    spacing: float | None = None,
    scales: float | None = None,
    novar: bool = False,
    dt: float | None = None,
    tol: float | None = None,
    center: bool = False,
    noscale: bool = False,
    noiscale: bool = False,
    num_transforms: float | None = None,
    area: float | None = None,
    nlarea: float | None = None,
    levels: float | None = None,
    intensity: float | None = None,
    reduce: float | None = None,
    n_samples: float | None = None,
    norm: str | None = None,
    trans: float | None = None,
    steps: float | None = None,
    long_reg: str | None = None,
    cpfile: InputPathType | None = None,
    translation_vector: list[float] | None = None,
    rotation_vector: list[float] | None = None,
    xform: str | None = None,
    blur: float | None = None,
    diagno: bool = False,
    s: float | None = None,
    max_angle: float | None = None,
    niters: float | None = None,
    write_iters: float | None = None,
    ctl_point_pct: float | None = None,
    momentum: float | None = None,
    threads: float | None = None,
) -> MriEmRegisterParameters:
    """
    Build parameters.
    
    Args:
        input_volume: Input brain volume.
        template_gca: Template GCA file.
        output_transform: Output transform name.
        distance: Distance.
        nomap: No map.
        flash: Use FLASH forward model to predict intensity values.
        mask: Use volname as a mask.
        skull: Align to atlas containing skull (uns=5).
        uns: Align to atlas containing skull setting unknown_nbr_spacing =\
            nbrspacing.
        diag: Open diagfile for writing.
        debug_voxel: Debug voxel (x, y, z).
        debug_label: Debug label (label).
        tr: Use TR msec.
        te: Use TE msec.
        alpha: Use alpha degrees.
        example: Use T1 and seg as example T1 and segmentations respectively.
        samples: Write control points to fname.
        fsamples: Write transformed control points to fname.
        nsamples: Write transformed normalization control points to fname.
        contrast: Use contrast to find labels.
        flash_parms: Use FLASH forward model and tissue parms in parameterfile\
            to predict intensity values.
        transonly: Only compute translation parameters.
        write_mean: Write GCA means to fname.
        prior: Use prior threshold min_prior.
        spacing: Use max GCA spacing.
        scales: Find optimal linear transform over int scales.
        novar: Do not use variance estimates.
        dt: DT parameter.
        tol: Tolerance.
        center: Use GCA centroid as origin of transform.
        noscale: Disable scaling.
        noiscale: Disable intensity scaling.
        num_transforms: Find a total of num_xforms linear transforms.
        area: Area.
        nlarea: Non-linear area.
        levels: Levels.
        intensity: Intensity.
        reduce: Reduce input images nreductions times before aligning.
        n_samples: Using n samples of GCA.
        norm: Normalize intensity and write to fname.
        trans: Setting max translation search range to be max_trans.
        steps: Taking max_angles angular steps.
        long_reg: Longitudinal: read previously computed atlas xform and apply\
            registration long_reg.
        cpfile: Read manually defined control points from cpfile.
        translation_vector: Translation vector (tx, ty, tz).
        rotation_vector: Rotation vector (rx, ry, rz).
        xform: Using previously computed transform xform.
        blur: Blurring input image with sigma=blur_sigma.
        diagno: Diago flag (unspecified function).
        s: Max angles.
        max_angle: Max angle for rotational search in radians (def=15 deg).
        niters: Niterations = niters.
        write_iters: Write iterations = write_iters.
        ctl_point_pct: Use top pct percent wm points as control points.
        momentum: Set momentum.
        threads: Number of threads (nompthreads).
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mri_em_register",
        "input_volume": input_volume,
        "template_gca": template_gca,
        "output_transform": output_transform,
        "nomap": nomap,
        "flash": flash,
        "skull": skull,
        "contrast": contrast,
        "transonly": transonly,
        "novar": novar,
        "center": center,
        "noscale": noscale,
        "noiscale": noiscale,
        "diagno": diagno,
    }
    if distance is not None:
        params["distance"] = distance
    if mask is not None:
        params["mask"] = mask
    if uns is not None:
        params["uns"] = uns
    if diag is not None:
        params["diag"] = diag
    if debug_voxel is not None:
        params["debug_voxel"] = debug_voxel
    if debug_label is not None:
        params["debug_label"] = debug_label
    if tr is not None:
        params["tr"] = tr
    if te is not None:
        params["te"] = te
    if alpha is not None:
        params["alpha"] = alpha
    if example is not None:
        params["example"] = example
    if samples is not None:
        params["samples"] = samples
    if fsamples is not None:
        params["fsamples"] = fsamples
    if nsamples is not None:
        params["nsamples"] = nsamples
    if flash_parms is not None:
        params["flash_parms"] = flash_parms
    if write_mean is not None:
        params["write_mean"] = write_mean
    if prior is not None:
        params["prior"] = prior
    if spacing is not None:
        params["spacing"] = spacing
    if scales is not None:
        params["scales"] = scales
    if dt is not None:
        params["dt"] = dt
    if tol is not None:
        params["tol"] = tol
    if num_transforms is not None:
        params["num_transforms"] = num_transforms
    if area is not None:
        params["area"] = area
    if nlarea is not None:
        params["nlarea"] = nlarea
    if levels is not None:
        params["levels"] = levels
    if intensity is not None:
        params["intensity"] = intensity
    if reduce is not None:
        params["reduce"] = reduce
    if n_samples is not None:
        params["n_samples"] = n_samples
    if norm is not None:
        params["norm"] = norm
    if trans is not None:
        params["trans"] = trans
    if steps is not None:
        params["steps"] = steps
    if long_reg is not None:
        params["long_reg"] = long_reg
    if cpfile is not None:
        params["cpfile"] = cpfile
    if translation_vector is not None:
        params["translation_vector"] = translation_vector
    if rotation_vector is not None:
        params["rotation_vector"] = rotation_vector
    if xform is not None:
        params["xform"] = xform
    if blur is not None:
        params["blur"] = blur
    if s is not None:
        params["s"] = s
    if max_angle is not None:
        params["max_angle"] = max_angle
    if niters is not None:
        params["niters"] = niters
    if write_iters is not None:
        params["write_iters"] = write_iters
    if ctl_point_pct is not None:
        params["ctl_point_pct"] = ctl_point_pct
    if momentum is not None:
        params["momentum"] = momentum
    if threads is not None:
        params["threads"] = threads
    return params


def mri_em_register_cargs(
    params: MriEmRegisterParameters,
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
    cargs.append("mri_em_register")
    cargs.append(execution.input_file(params.get("input_volume")))
    cargs.append(execution.input_file(params.get("template_gca")))
    cargs.append(params.get("output_transform"))
    if params.get("distance") is not None:
        cargs.extend([
            "-dist",
            str(params.get("distance"))
        ])
    if params.get("nomap"):
        cargs.append("-nomap")
    if params.get("flash"):
        cargs.append("-flash")
    if params.get("mask") is not None:
        cargs.extend([
            "-mask",
            execution.input_file(params.get("mask"))
        ])
    if params.get("skull"):
        cargs.append("-skull")
    if params.get("uns") is not None:
        cargs.extend([
            "-uns",
            str(params.get("uns"))
        ])
    if params.get("diag") is not None:
        cargs.extend([
            "-diag",
            params.get("diag")
        ])
    if params.get("debug_voxel") is not None:
        cargs.extend([
            "-debug_voxel",
            *map(str, params.get("debug_voxel"))
        ])
    if params.get("debug_label") is not None:
        cargs.extend([
            "-debug_label",
            str(params.get("debug_label"))
        ])
    if params.get("tr") is not None:
        cargs.extend([
            "-tr",
            str(params.get("tr"))
        ])
    if params.get("te") is not None:
        cargs.extend([
            "-te",
            str(params.get("te"))
        ])
    if params.get("alpha") is not None:
        cargs.extend([
            "-alpha",
            str(params.get("alpha"))
        ])
    if params.get("example") is not None:
        cargs.extend([
            "-example",
            *[execution.input_file(f) for f in params.get("example")]
        ])
    if params.get("samples") is not None:
        cargs.extend([
            "-samples",
            params.get("samples")
        ])
    if params.get("fsamples") is not None:
        cargs.extend([
            "-fsamples",
            params.get("fsamples")
        ])
    if params.get("nsamples") is not None:
        cargs.extend([
            "-nsamples",
            params.get("nsamples")
        ])
    if params.get("contrast"):
        cargs.append("-contrast")
    if params.get("flash_parms") is not None:
        cargs.extend([
            "-flash_parms",
            execution.input_file(params.get("flash_parms"))
        ])
    if params.get("transonly"):
        cargs.append("-transonly")
    if params.get("write_mean") is not None:
        cargs.extend([
            "-write_mean",
            params.get("write_mean")
        ])
    if params.get("prior") is not None:
        cargs.extend([
            "-prior",
            str(params.get("prior"))
        ])
    if params.get("spacing") is not None:
        cargs.extend([
            "-spacing",
            str(params.get("spacing"))
        ])
    if params.get("scales") is not None:
        cargs.extend([
            "-scales",
            str(params.get("scales"))
        ])
    if params.get("novar"):
        cargs.append("-novar")
    if params.get("dt") is not None:
        cargs.extend([
            "-dt",
            str(params.get("dt"))
        ])
    if params.get("tol") is not None:
        cargs.extend([
            "-tol",
            str(params.get("tol"))
        ])
    if params.get("center"):
        cargs.append("-center")
    if params.get("noscale"):
        cargs.append("-noscale")
    if params.get("noiscale"):
        cargs.append("-noiscale")
    if params.get("num_transforms") is not None:
        cargs.extend([
            "-num",
            str(params.get("num_transforms"))
        ])
    if params.get("area") is not None:
        cargs.extend([
            "-area",
            str(params.get("area"))
        ])
    if params.get("nlarea") is not None:
        cargs.extend([
            "-nlarea",
            str(params.get("nlarea"))
        ])
    if params.get("levels") is not None:
        cargs.extend([
            "-levels",
            str(params.get("levels"))
        ])
    if params.get("intensity") is not None:
        cargs.extend([
            "-intensity",
            str(params.get("intensity"))
        ])
    if params.get("reduce") is not None:
        cargs.extend([
            "-reduce",
            str(params.get("reduce"))
        ])
    if params.get("n_samples") is not None:
        cargs.extend([
            "-nsamples",
            str(params.get("n_samples"))
        ])
    if params.get("norm") is not None:
        cargs.extend([
            "-norm",
            params.get("norm")
        ])
    if params.get("trans") is not None:
        cargs.extend([
            "-trans",
            str(params.get("trans"))
        ])
    if params.get("steps") is not None:
        cargs.extend([
            "-steps",
            str(params.get("steps"))
        ])
    if params.get("long_reg") is not None:
        cargs.extend([
            "-l",
            params.get("long_reg")
        ])
    if params.get("cpfile") is not None:
        cargs.extend([
            "-f",
            execution.input_file(params.get("cpfile"))
        ])
    if params.get("translation_vector") is not None:
        cargs.extend([
            "-d",
            *map(str, params.get("translation_vector"))
        ])
    if params.get("rotation_vector") is not None:
        cargs.extend([
            "-r",
            *map(str, params.get("rotation_vector"))
        ])
    if params.get("xform") is not None:
        cargs.extend([
            "-t",
            params.get("xform")
        ])
    if params.get("blur") is not None:
        cargs.extend([
            "-b",
            str(params.get("blur"))
        ])
    if params.get("diagno"):
        cargs.append("-v")
    if params.get("s") is not None:
        cargs.extend([
            "-s",
            str(params.get("s"))
        ])
    if params.get("max_angle") is not None:
        cargs.extend([
            "-max_angle",
            str(params.get("max_angle"))
        ])
    if params.get("niters") is not None:
        cargs.extend([
            "-n",
            str(params.get("niters"))
        ])
    if params.get("write_iters") is not None:
        cargs.extend([
            "-w",
            str(params.get("write_iters"))
        ])
    if params.get("ctl_point_pct") is not None:
        cargs.extend([
            "-p",
            str(params.get("ctl_point_pct"))
        ])
    if params.get("momentum") is not None:
        cargs.extend([
            "-m",
            str(params.get("momentum"))
        ])
    if params.get("threads") is not None:
        cargs.extend([
            "-threads",
            str(params.get("threads"))
        ])
    return cargs


def mri_em_register_outputs(
    params: MriEmRegisterParameters,
    execution: Execution,
) -> MriEmRegisterOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MriEmRegisterOutputs(
        root=execution.output_file("."),
        output_transform_file=execution.output_file(params.get("output_transform") + ".lta"),
    )
    return ret


def mri_em_register_execute(
    params: MriEmRegisterParameters,
    execution: Execution,
) -> MriEmRegisterOutputs:
    """
    This program creates a transform in lta format.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MriEmRegisterOutputs`).
    """
    params = execution.params(params)
    cargs = mri_em_register_cargs(params, execution)
    ret = mri_em_register_outputs(params, execution)
    execution.run(cargs)
    return ret


def mri_em_register(
    input_volume: InputPathType,
    template_gca: InputPathType,
    output_transform: str,
    distance: float | None = None,
    nomap: bool = False,
    flash: bool = False,
    mask: InputPathType | None = None,
    skull: bool = False,
    uns: float | None = None,
    diag: str | None = None,
    debug_voxel: list[float] | None = None,
    debug_label: float | None = None,
    tr: float | None = None,
    te: float | None = None,
    alpha: float | None = None,
    example: list[InputPathType] | None = None,
    samples: str | None = None,
    fsamples: str | None = None,
    nsamples: str | None = None,
    contrast: bool = False,
    flash_parms: InputPathType | None = None,
    transonly: bool = False,
    write_mean: str | None = None,
    prior: float | None = None,
    spacing: float | None = None,
    scales: float | None = None,
    novar: bool = False,
    dt: float | None = None,
    tol: float | None = None,
    center: bool = False,
    noscale: bool = False,
    noiscale: bool = False,
    num_transforms: float | None = None,
    area: float | None = None,
    nlarea: float | None = None,
    levels: float | None = None,
    intensity: float | None = None,
    reduce: float | None = None,
    n_samples: float | None = None,
    norm: str | None = None,
    trans: float | None = None,
    steps: float | None = None,
    long_reg: str | None = None,
    cpfile: InputPathType | None = None,
    translation_vector: list[float] | None = None,
    rotation_vector: list[float] | None = None,
    xform: str | None = None,
    blur: float | None = None,
    diagno: bool = False,
    s: float | None = None,
    max_angle: float | None = None,
    niters: float | None = None,
    write_iters: float | None = None,
    ctl_point_pct: float | None = None,
    momentum: float | None = None,
    threads: float | None = None,
    runner: Runner | None = None,
) -> MriEmRegisterOutputs:
    """
    This program creates a transform in lta format.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_volume: Input brain volume.
        template_gca: Template GCA file.
        output_transform: Output transform name.
        distance: Distance.
        nomap: No map.
        flash: Use FLASH forward model to predict intensity values.
        mask: Use volname as a mask.
        skull: Align to atlas containing skull (uns=5).
        uns: Align to atlas containing skull setting unknown_nbr_spacing =\
            nbrspacing.
        diag: Open diagfile for writing.
        debug_voxel: Debug voxel (x, y, z).
        debug_label: Debug label (label).
        tr: Use TR msec.
        te: Use TE msec.
        alpha: Use alpha degrees.
        example: Use T1 and seg as example T1 and segmentations respectively.
        samples: Write control points to fname.
        fsamples: Write transformed control points to fname.
        nsamples: Write transformed normalization control points to fname.
        contrast: Use contrast to find labels.
        flash_parms: Use FLASH forward model and tissue parms in parameterfile\
            to predict intensity values.
        transonly: Only compute translation parameters.
        write_mean: Write GCA means to fname.
        prior: Use prior threshold min_prior.
        spacing: Use max GCA spacing.
        scales: Find optimal linear transform over int scales.
        novar: Do not use variance estimates.
        dt: DT parameter.
        tol: Tolerance.
        center: Use GCA centroid as origin of transform.
        noscale: Disable scaling.
        noiscale: Disable intensity scaling.
        num_transforms: Find a total of num_xforms linear transforms.
        area: Area.
        nlarea: Non-linear area.
        levels: Levels.
        intensity: Intensity.
        reduce: Reduce input images nreductions times before aligning.
        n_samples: Using n samples of GCA.
        norm: Normalize intensity and write to fname.
        trans: Setting max translation search range to be max_trans.
        steps: Taking max_angles angular steps.
        long_reg: Longitudinal: read previously computed atlas xform and apply\
            registration long_reg.
        cpfile: Read manually defined control points from cpfile.
        translation_vector: Translation vector (tx, ty, tz).
        rotation_vector: Rotation vector (rx, ry, rz).
        xform: Using previously computed transform xform.
        blur: Blurring input image with sigma=blur_sigma.
        diagno: Diago flag (unspecified function).
        s: Max angles.
        max_angle: Max angle for rotational search in radians (def=15 deg).
        niters: Niterations = niters.
        write_iters: Write iterations = write_iters.
        ctl_point_pct: Use top pct percent wm points as control points.
        momentum: Set momentum.
        threads: Number of threads (nompthreads).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriEmRegisterOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_EM_REGISTER_METADATA)
    params = mri_em_register_params(
        input_volume=input_volume,
        template_gca=template_gca,
        output_transform=output_transform,
        distance=distance,
        nomap=nomap,
        flash=flash,
        mask=mask,
        skull=skull,
        uns=uns,
        diag=diag,
        debug_voxel=debug_voxel,
        debug_label=debug_label,
        tr=tr,
        te=te,
        alpha=alpha,
        example=example,
        samples=samples,
        fsamples=fsamples,
        nsamples=nsamples,
        contrast=contrast,
        flash_parms=flash_parms,
        transonly=transonly,
        write_mean=write_mean,
        prior=prior,
        spacing=spacing,
        scales=scales,
        novar=novar,
        dt=dt,
        tol=tol,
        center=center,
        noscale=noscale,
        noiscale=noiscale,
        num_transforms=num_transforms,
        area=area,
        nlarea=nlarea,
        levels=levels,
        intensity=intensity,
        reduce=reduce,
        n_samples=n_samples,
        norm=norm,
        trans=trans,
        steps=steps,
        long_reg=long_reg,
        cpfile=cpfile,
        translation_vector=translation_vector,
        rotation_vector=rotation_vector,
        xform=xform,
        blur=blur,
        diagno=diagno,
        s=s,
        max_angle=max_angle,
        niters=niters,
        write_iters=write_iters,
        ctl_point_pct=ctl_point_pct,
        momentum=momentum,
        threads=threads,
    )
    return mri_em_register_execute(params, execution)


__all__ = [
    "MRI_EM_REGISTER_METADATA",
    "MriEmRegisterOutputs",
    "MriEmRegisterParameters",
    "mri_em_register",
    "mri_em_register_params",
]
