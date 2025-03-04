# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

PROBTRACKX_METADATA = Metadata(
    id="053d5bf02cc2ecddcdfc27a671338716940fbabe.boutiques",
    name="probtrackx",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)


ProbtrackxParameters = typing.TypedDict('ProbtrackxParameters', {
    "__STYX_TYPE__": typing.Literal["probtrackx"],
    "samples": InputPathType,
    "mask": InputPathType,
    "seed": InputPathType,
    "out": str,
    "verbose": typing.NotRequired[int | None],
    "targetmasks": typing.NotRequired[InputPathType | None],
    "mask2": typing.NotRequired[InputPathType | None],
    "waypoints": typing.NotRequired[InputPathType | None],
    "network": bool,
    "mesh": typing.NotRequired[InputPathType | None],
    "seedref": typing.NotRequired[InputPathType | None],
    "dir": typing.NotRequired[str | None],
    "forcedir": bool,
    "opd": bool,
    "pd": bool,
    "os2t": bool,
    "avoid": typing.NotRequired[InputPathType | None],
    "stop": typing.NotRequired[InputPathType | None],
    "xfm": typing.NotRequired[InputPathType | None],
    "invxfm": typing.NotRequired[InputPathType | None],
    "nsamples": typing.NotRequired[int | None],
    "nsteps": typing.NotRequired[int | None],
    "distthresh": typing.NotRequired[float | None],
    "cthr": typing.NotRequired[float | None],
    "fibthresh": typing.NotRequired[float | None],
    "sampvox": bool,
    "steplength": typing.NotRequired[float | None],
    "loopcheck": bool,
    "usef": bool,
    "randfib": typing.NotRequired[int | None],
    "fibst": typing.NotRequired[int | None],
    "modeuler": bool,
    "rseed": typing.NotRequired[int | None],
    "s2tastext": bool,
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
        "probtrackx": probtrackx_cargs,
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


class ProbtrackxOutputs(typing.NamedTuple):
    """
    Output object returned when calling `probtrackx(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def probtrackx_params(
    samples: InputPathType,
    mask: InputPathType,
    seed: InputPathType,
    out: str = "fdt_paths",
    verbose: int | None = None,
    targetmasks: InputPathType | None = None,
    mask2: InputPathType | None = None,
    waypoints: InputPathType | None = None,
    network: bool = False,
    mesh: InputPathType | None = None,
    seedref: InputPathType | None = None,
    dir_: str | None = "logdir",
    forcedir: bool = False,
    opd: bool = False,
    pd: bool = False,
    os2t: bool = False,
    avoid: InputPathType | None = None,
    stop: InputPathType | None = None,
    xfm: InputPathType | None = None,
    invxfm: InputPathType | None = None,
    nsamples: int | None = 5000,
    nsteps: int | None = 2000,
    distthresh: float | None = 0,
    cthr: float | None = 0.2,
    fibthresh: float | None = 0.01,
    sampvox: bool = False,
    steplength: float | None = 0.5,
    loopcheck: bool = False,
    usef: bool = False,
    randfib: int | None = 0,
    fibst: int | None = 1,
    modeuler: bool = False,
    rseed: int | None = None,
    s2tastext: bool = False,
) -> ProbtrackxParameters:
    """
    Build parameters.
    
    Args:
        samples: Basename for samples files.
        mask: Bet binary mask file in diffusion space.
        seed: Seed volume, or voxel, or ascii file with multiple volumes, or\
            freesurfer label file.
        out: Output file (default='fdt_paths').
        verbose: Verbose level, [0-2].
        targetmasks: File containing a list of target masks - required for\
            seeds_to_targets classification.
        mask2: Second mask in twomask_symm mode.
        waypoints: Waypoint mask or ascii list of waypoint masks - only keep\
            paths going through ALL the masks.
        network: Activate network mode - only keep paths going through at least\
            one seed mask (required if multiple seed masks).
        mesh: Freesurfer-type surface descriptor (in ascii format).
        seedref: Reference vol to define seed space in simple mode - diffusion\
            space assumed if absent.
        dir_: Directory to put the final volumes in - code makes this directory\
            - default='logdir'.
        forcedir: Use the actual directory name given - i.e. don't add + to\
            make a new directory.
        opd: Output path distribution.
        pd: Correct path distribution for the length of the pathways.
        os2t: Output seeds to targets.
        avoid: Reject pathways passing through locations given by this mask.
        stop: Stop tracking at locations given by this mask file.
        xfm: Transform taking seed space to DTI space (either FLIRT matrix or\
            FNIRT warpfield) - default is identity.
        invxfm: Transform taking DTI space to seed space (compulsory when using\
            a warpfield for seeds_to_dti).
        nsamples: Number of samples - default=5000.
        nsteps: Number of steps per sample - default=2000.
        distthresh: Discards samples shorter than this threshold (in mm -\
            default=0).
        cthr: Curvature threshold - default=0.2.
        fibthresh: Volume fraction before subsidary fibre orientations are\
            considered - default=0.01.
        sampvox: Sample random points within seed voxels.
        steplength: Steplength in mm - default=0.5.
        loopcheck: Perform loopchecks on paths - slower, but allows lower\
            curvature threshold.
        usef: Use anisotropy to constrain tracking.
        randfib: Default 0. Set to 1 to randomly sample initial fibres (with f\
            > fibthresh). Set to 2 to sample in proportion fibres (with\
            f>fibthresh) to f. Set to 3 to sample ALL populations at random (even\
            if f<fibthresh).
        fibst: Force a starting fibre for tracking - default=1, i.e. first\
            fibre orientation. Only works if randfib==0.
        modeuler: Use modified euler streamlining.
        rseed: Random seed.
        s2tastext: Output seed-to-target counts as a text file (useful when\
            seeding from a mesh).
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "probtrackx",
        "samples": samples,
        "mask": mask,
        "seed": seed,
        "out": out,
        "network": network,
        "forcedir": forcedir,
        "opd": opd,
        "pd": pd,
        "os2t": os2t,
        "sampvox": sampvox,
        "loopcheck": loopcheck,
        "usef": usef,
        "modeuler": modeuler,
        "s2tastext": s2tastext,
    }
    if verbose is not None:
        params["verbose"] = verbose
    if targetmasks is not None:
        params["targetmasks"] = targetmasks
    if mask2 is not None:
        params["mask2"] = mask2
    if waypoints is not None:
        params["waypoints"] = waypoints
    if mesh is not None:
        params["mesh"] = mesh
    if seedref is not None:
        params["seedref"] = seedref
    if dir_ is not None:
        params["dir"] = dir_
    if avoid is not None:
        params["avoid"] = avoid
    if stop is not None:
        params["stop"] = stop
    if xfm is not None:
        params["xfm"] = xfm
    if invxfm is not None:
        params["invxfm"] = invxfm
    if nsamples is not None:
        params["nsamples"] = nsamples
    if nsteps is not None:
        params["nsteps"] = nsteps
    if distthresh is not None:
        params["distthresh"] = distthresh
    if cthr is not None:
        params["cthr"] = cthr
    if fibthresh is not None:
        params["fibthresh"] = fibthresh
    if steplength is not None:
        params["steplength"] = steplength
    if randfib is not None:
        params["randfib"] = randfib
    if fibst is not None:
        params["fibst"] = fibst
    if rseed is not None:
        params["rseed"] = rseed
    return params


def probtrackx_cargs(
    params: ProbtrackxParameters,
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
    cargs.append("probtrackx")
    cargs.extend([
        "-s",
        execution.input_file(params.get("samples"))
    ])
    cargs.extend([
        "-m",
        execution.input_file(params.get("mask"))
    ])
    cargs.extend([
        "-x",
        execution.input_file(params.get("seed"))
    ])
    cargs.extend([
        "-o",
        params.get("out")
    ])
    if params.get("verbose") is not None:
        cargs.extend([
            "--verbose",
            str(params.get("verbose"))
        ])
    if params.get("targetmasks") is not None:
        cargs.extend([
            "--targetmasks",
            execution.input_file(params.get("targetmasks"))
        ])
    if params.get("mask2") is not None:
        cargs.extend([
            "--mask2",
            execution.input_file(params.get("mask2"))
        ])
    if params.get("waypoints") is not None:
        cargs.extend([
            "--waypoints",
            execution.input_file(params.get("waypoints"))
        ])
    if params.get("network"):
        cargs.append("--network")
    if params.get("mesh") is not None:
        cargs.extend([
            "--mesh",
            execution.input_file(params.get("mesh"))
        ])
    if params.get("seedref") is not None:
        cargs.extend([
            "--seedref",
            execution.input_file(params.get("seedref"))
        ])
    if params.get("dir") is not None:
        cargs.extend([
            "--dir",
            params.get("dir")
        ])
    if params.get("forcedir"):
        cargs.append("--forcedir")
    if params.get("opd"):
        cargs.append("--opd")
    if params.get("pd"):
        cargs.append("--pd")
    if params.get("os2t"):
        cargs.append("--os2t")
    if params.get("avoid") is not None:
        cargs.extend([
            "--avoid",
            execution.input_file(params.get("avoid"))
        ])
    if params.get("stop") is not None:
        cargs.extend([
            "--stop",
            execution.input_file(params.get("stop"))
        ])
    if params.get("xfm") is not None:
        cargs.extend([
            "--xfm",
            execution.input_file(params.get("xfm"))
        ])
    if params.get("invxfm") is not None:
        cargs.extend([
            "--invxfm",
            execution.input_file(params.get("invxfm"))
        ])
    if params.get("nsamples") is not None:
        cargs.extend([
            "-P",
            str(params.get("nsamples"))
        ])
    if params.get("nsteps") is not None:
        cargs.extend([
            "-S",
            str(params.get("nsteps"))
        ])
    if params.get("distthresh") is not None:
        cargs.extend([
            "--distthresh",
            str(params.get("distthresh"))
        ])
    if params.get("cthr") is not None:
        cargs.extend([
            "-c",
            str(params.get("cthr"))
        ])
    if params.get("fibthresh") is not None:
        cargs.extend([
            "--fibthresh",
            str(params.get("fibthresh"))
        ])
    if params.get("sampvox"):
        cargs.append("--sampvox")
    if params.get("steplength") is not None:
        cargs.extend([
            "--steplength",
            str(params.get("steplength"))
        ])
    if params.get("loopcheck"):
        cargs.append("-l")
    if params.get("usef"):
        cargs.append("-f")
    if params.get("randfib") is not None:
        cargs.extend([
            "--randfib",
            str(params.get("randfib"))
        ])
    if params.get("fibst") is not None:
        cargs.extend([
            "--fibst",
            str(params.get("fibst"))
        ])
    if params.get("modeuler"):
        cargs.append("--modeuler")
    if params.get("rseed") is not None:
        cargs.extend([
            "--rseed",
            str(params.get("rseed"))
        ])
    if params.get("s2tastext"):
        cargs.append("--s2tastext")
    return cargs


def probtrackx_outputs(
    params: ProbtrackxParameters,
    execution: Execution,
) -> ProbtrackxOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = ProbtrackxOutputs(
        root=execution.output_file("."),
    )
    return ret


def probtrackx_execute(
    params: ProbtrackxParameters,
    execution: Execution,
) -> ProbtrackxOutputs:
    """
    Streamlines tracking algorithm for probabilistic tractography.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `ProbtrackxOutputs`).
    """
    params = execution.params(params)
    cargs = probtrackx_cargs(params, execution)
    ret = probtrackx_outputs(params, execution)
    execution.run(cargs)
    return ret


def probtrackx(
    samples: InputPathType,
    mask: InputPathType,
    seed: InputPathType,
    out: str = "fdt_paths",
    verbose: int | None = None,
    targetmasks: InputPathType | None = None,
    mask2: InputPathType | None = None,
    waypoints: InputPathType | None = None,
    network: bool = False,
    mesh: InputPathType | None = None,
    seedref: InputPathType | None = None,
    dir_: str | None = "logdir",
    forcedir: bool = False,
    opd: bool = False,
    pd: bool = False,
    os2t: bool = False,
    avoid: InputPathType | None = None,
    stop: InputPathType | None = None,
    xfm: InputPathType | None = None,
    invxfm: InputPathType | None = None,
    nsamples: int | None = 5000,
    nsteps: int | None = 2000,
    distthresh: float | None = 0,
    cthr: float | None = 0.2,
    fibthresh: float | None = 0.01,
    sampvox: bool = False,
    steplength: float | None = 0.5,
    loopcheck: bool = False,
    usef: bool = False,
    randfib: int | None = 0,
    fibst: int | None = 1,
    modeuler: bool = False,
    rseed: int | None = None,
    s2tastext: bool = False,
    runner: Runner | None = None,
) -> ProbtrackxOutputs:
    """
    Streamlines tracking algorithm for probabilistic tractography.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        samples: Basename for samples files.
        mask: Bet binary mask file in diffusion space.
        seed: Seed volume, or voxel, or ascii file with multiple volumes, or\
            freesurfer label file.
        out: Output file (default='fdt_paths').
        verbose: Verbose level, [0-2].
        targetmasks: File containing a list of target masks - required for\
            seeds_to_targets classification.
        mask2: Second mask in twomask_symm mode.
        waypoints: Waypoint mask or ascii list of waypoint masks - only keep\
            paths going through ALL the masks.
        network: Activate network mode - only keep paths going through at least\
            one seed mask (required if multiple seed masks).
        mesh: Freesurfer-type surface descriptor (in ascii format).
        seedref: Reference vol to define seed space in simple mode - diffusion\
            space assumed if absent.
        dir_: Directory to put the final volumes in - code makes this directory\
            - default='logdir'.
        forcedir: Use the actual directory name given - i.e. don't add + to\
            make a new directory.
        opd: Output path distribution.
        pd: Correct path distribution for the length of the pathways.
        os2t: Output seeds to targets.
        avoid: Reject pathways passing through locations given by this mask.
        stop: Stop tracking at locations given by this mask file.
        xfm: Transform taking seed space to DTI space (either FLIRT matrix or\
            FNIRT warpfield) - default is identity.
        invxfm: Transform taking DTI space to seed space (compulsory when using\
            a warpfield for seeds_to_dti).
        nsamples: Number of samples - default=5000.
        nsteps: Number of steps per sample - default=2000.
        distthresh: Discards samples shorter than this threshold (in mm -\
            default=0).
        cthr: Curvature threshold - default=0.2.
        fibthresh: Volume fraction before subsidary fibre orientations are\
            considered - default=0.01.
        sampvox: Sample random points within seed voxels.
        steplength: Steplength in mm - default=0.5.
        loopcheck: Perform loopchecks on paths - slower, but allows lower\
            curvature threshold.
        usef: Use anisotropy to constrain tracking.
        randfib: Default 0. Set to 1 to randomly sample initial fibres (with f\
            > fibthresh). Set to 2 to sample in proportion fibres (with\
            f>fibthresh) to f. Set to 3 to sample ALL populations at random (even\
            if f<fibthresh).
        fibst: Force a starting fibre for tracking - default=1, i.e. first\
            fibre orientation. Only works if randfib==0.
        modeuler: Use modified euler streamlining.
        rseed: Random seed.
        s2tastext: Output seed-to-target counts as a text file (useful when\
            seeding from a mesh).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `ProbtrackxOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(PROBTRACKX_METADATA)
    params = probtrackx_params(
        samples=samples,
        mask=mask,
        seed=seed,
        out=out,
        verbose=verbose,
        targetmasks=targetmasks,
        mask2=mask2,
        waypoints=waypoints,
        network=network,
        mesh=mesh,
        seedref=seedref,
        dir_=dir_,
        forcedir=forcedir,
        opd=opd,
        pd=pd,
        os2t=os2t,
        avoid=avoid,
        stop=stop,
        xfm=xfm,
        invxfm=invxfm,
        nsamples=nsamples,
        nsteps=nsteps,
        distthresh=distthresh,
        cthr=cthr,
        fibthresh=fibthresh,
        sampvox=sampvox,
        steplength=steplength,
        loopcheck=loopcheck,
        usef=usef,
        randfib=randfib,
        fibst=fibst,
        modeuler=modeuler,
        rseed=rseed,
        s2tastext=s2tastext,
    )
    return probtrackx_execute(params, execution)


__all__ = [
    "PROBTRACKX_METADATA",
    "ProbtrackxOutputs",
    "ProbtrackxParameters",
    "probtrackx",
    "probtrackx_params",
]
